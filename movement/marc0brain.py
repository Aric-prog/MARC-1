import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 


motorLeftA = 13
motorLeftB = 15
motorLeftE = 11

motorRightA = 18
motorRightB = 16
motorRightE = 22

motorPins = [motorLeftA, motorLeftB, motorLeftE, motorRightA, motorRightB, motorRightE]

# Pins for Infrared sensors
frontIRSensor = 8
backIRSensor = 7
IRSensorPins = [frontIRSensor, backIRSensor]

def setup():
    # GPIO Numbering
	GPIO.setmode(GPIO.BOARD)				

    # set all motor pins as outputs
	GPIO.setup(motorPins, GPIO.OUT) 

    # set all infrared sensor pins as inputs
    GPIO.setup(IRSensorPins, GPIO.IN)

def runWheelForward(motorA, motorB, motorE):
    GPIO.output(motorE,GPIO.HIGH)
    GPIO.output(motorA,GPIO.HIGH)
    GPIO.output(motorB,GPIO.LOW)

def runWheelReverse(motorA, motorB, motorE):
    GPIO.output(motorE,GPIO.HIGH)
    GPIO.output(motorA,GPIO.LOW)
    GPIO.output(motorB,GPIO.HIGH)

def forward():
    runWheelForward(motorLeftA, motorLeftB, motorLeftE)
    runWheelForward(motorRightA, motorRightB, motorRightE)

def reverse():
    runWheelReverse(motorLeftA, motorLeftB, motorLeftE)
    runWheelReverse(motorRightA, motorRightB, motorRightE)

def stopMotor(motorLeftE, motorRightE):
    GPIO.output(motorLeftE,GPIO.LOW)
    GPIO.output(motorRightE,GPIO.LOW) 

def turnRight():
    runWheelForward(motorLeftA, motorLeftB, motorLeftE)
    runWheelReverse(motorRightA, motorRightB, motorRightE)

def turnLeft():
    runWheelForward(motorRightA, motorRightB, motorRightE)
    runWheelReverse(motorLeftA, motorLeftB, motorLeftE)
 
def loop():
    while True:
        if GPIO.input(frontIRSensor):
            forward()
            sleep(2)
            turnLeft()
            sleep(2)
            turnRight()
            sleep(2)
            reverse()
            sleep(2)
        else:
            stopMotor(motorLeftE, motorRightE)

def destroy():	
	GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
    	loop()
  	except KeyboardInterrupt:
		destroy()