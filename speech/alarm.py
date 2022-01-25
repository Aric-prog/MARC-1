from threading import Timer
import datetime
from playsound import playsound
# Assuming this is proper military time
def alarm(milTime):
    milTime.rjust(4, '0')
    hours = int(milTime[0:2])
    minutes = int(milTime[2:4])
    
    if(minutes >= 60):return
    elif(hours >= 24):return

    currentTime = datetime.datetime.now()
    targetTime = currentTime.replace(hour=hours, minute=minutes, second=0, microsecond=0)
    if(targetTime < currentTime):
        targetTime = targetTime + datetime.timedelta(days=1)

    dt = targetTime - currentTime
    t = Timer(dt.seconds, soundAlarm)
    t.start()

def soundAlarm():
    playsound('alarm.mp3', False)
    print('Alarm will ring in this function')
