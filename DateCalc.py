# import time
# 
# 
# print(time.gmtime(0))
#  
# time_here = time.localtime()
# print(time_here)
#  
# print("year: ", time_here[0],time_here.tm_year)
# print("month:", time_here[1],time_here.tm_mon)
# print("day:", time_here[2],time_here.tm_mday)
# print("hour:", time_here[3],time_here.tm_hour)
# print("min:", time_here[4],time_here.tm_min)


import time
from time import process_time as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1,6)
time.sleep(wait_time)

start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()
# print("End time is " + str(end_time))
# print("local end time is " )
 
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("stopped at " + time.strftime("%X", time.localtime(end_time)))
 
print("Your reaction time was {}".format(end_time-start_time))