# import time
# 
# print("The epoch on this system is: " + time.strftime('%c',time.gmtime(0)))
# 
# print("The current timezone is {0} wih an offest of {1}".format(time.tzname[0],time.timezone))
# 
# if time.daylight!=0:
#     print("\t Daylight saving time is in effect for this location")
#     print("\tThe DST timezone is : "+ time.tzname[1])
# 
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
# print("UCT time is " + time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))

import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())