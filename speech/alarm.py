from threading import Timer
import time
import pytz
import datetime

# Assuming this is proper military time
def alarm(milTime):
    milTime.rjust(4, '0')
    hours = int(milTime[0:2])
    minutes = int(milTime[2:4])
    
    currentTime = datetime.datetime.now()
    targetTime = currentTime.replace(hour=hours, minute=minutes)
    if(targetTime < currentTime):
        targetTime = targetTime + datetime.timedelta(days=1)

    dt = targetTime - currentTime
    t = Timer(dt.seconds, soundAlarm)

def soundAlarm():
    print('alarm will ring in this function')

