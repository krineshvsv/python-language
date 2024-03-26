from datetime import datetime
from playsound import playsound
alaram_time=str(input("Enter time in the format 'HH:MM:SS AM/PM'\n"))
alaram_hour=alaram_time[0:2]
alaram_Minute=alaram_time[3:5]
alaram_second=alaram_time[6:8]
alaram_period=alaram_time[9:11].upper()
print("Your alaram is:")
print(f"{alaram_hour}:{alaram_Minute}:{alaram_second} {alaram_period}")
print("Setting up alaram...")
'''
#now:
    ->  "now()" is a method of the "datetime" class that returns the cureent date and time
        as a "datetime" object . it does not take any arguments.

#strftime: 
    -> "strftime()" is a method of the "datetime" class used to format a "datetime" object 
        as a string.
        ->the format string as an argument,which specifies how the date and time should be
            formatted.
        ->The format string consists of special formatting codes that starts with a "%" sign,
            such as "%I" for hour(12-hour clock),"%M" for minute, "%S" for second, and "%P"
            for the period(AM/PM).

'''
while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_seconds=now.strftime("%S")
    current_period=now.strftime("%p")
    if(alaram_period==current_period):
        if(alaram_hour==current_hour):
            if(alaram_Minute==current_minute):
                if(alaram_second==current_seconds):
                    print("Wake up!")
                    playsound('audio.mp3')
                    break;
