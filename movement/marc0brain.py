from turtle import done
import asyncio
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo

# Pins for Motor Driver Inputs

motorLeftA = 18
motorLeftB = 16
motorLeftE = 22

motorRightA = 13
motorRightB = 15
motorRightE = 11

SERVO_PIN = 37

motorPins = [motorLeftA, motorLeftB, motorLeftE,
             motorRightA, motorRightB, motorRightE]

# Pins for Infrared sensors
frontIRSensor = 8
backIRSensor = 10
IRSensorPins = [frontIRSensor, backIRSensor]

servo = Servo(SERVO_PIN)
servo.value = 0

def setup():
    # GPIO Numbering
    GPIO.setmode(GPIO.BOARD)

    # set all motor pins as outputs
    GPIO.setup(motorPins, GPIO.OUT)

    # set all infrared sensor pins as inputs
    GPIO.setup(IRSensorPins, GPIO.IN)


def runWheelForward(motorA, motorB, motorE):
    GPIO.output(motorE, GPIO.HIGH)
    GPIO.output(motorA, GPIO.HIGH)
    GPIO.output(motorB, GPIO.LOW)


def runWheelReverse(motorA, motorB, motorE):
    GPIO.output(motorE, GPIO.HIGH)
    GPIO.output(motorA, GPIO.LOW)
    GPIO.output(motorB, GPIO.HIGH)


def forward():
    runWheelForward(motorLeftA, motorLeftB, motorLeftE)
    runWheelForward(motorRightA, motorRightB, motorRightE)


def reverse():
    runWheelReverse(motorLeftA, motorLeftB, motorLeftE)
    runWheelReverse(motorRightA, motorRightB, motorRightE)


def stopMotor(motorLeftE, motorRightE):
    GPIO.output(motorLeftE, GPIO.LOW)
    GPIO.output(motorRightE, GPIO.LOW)


def turnRight():
    runWheelForward(motorLeftA, motorLeftB, motorLeftE)
    runWheelReverse(motorRightA, motorRightB, motorRightE)


def turnLeft():
    runWheelForward(motorRightA, motorRightB, motorRightE)
    runWheelReverse(motorLeftA, motorLeftB, motorLeftE)


async def generalMove(movementfunctionarg):
    movementfunctionarg()
    stopMotor()
    while (GPIO.input(frontIRSensor) and GPIO.input(backIRSensor)):
        movementfunctionarg()
        return 200

def rotateCamera(rotate):
    servo.value += max(-1, min(servo.value + rotate, 1))
    return 200

def loop():
    pass
    # while True:
    #     if GPIO.input(frontIRSensor):
    #         forward()
    #         sleep(2)
    #         turnLeft()
    #         sleep(2)
    #         turnRight()
    #         sleep(2)
    #         reverse()
    #         sleep(2)
    #     else:
    #         stopMotor(motorLeftE, motorRightE)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
