# import time
# from time import time as my_timer1
# from time import perf_counter as my_timer2
# from time import monotonic as my_timer3
# from time import process_time as my_timer4
# import random
# 
# input("Press enter to start")
# 
# wait_time = random.randint(1,6)
# time.sleep(wait_time)
# 
# start_time1 = my_timer1()
# start_time2 = my_timer2()
# start_time3 = my_timer3()
# start_time4 = my_timer4()
# input("Press enter to stop")
# 
# end_time1 = my_timer1()
# end_time2 = my_timer2()
# end_time3 = my_timer3()
# end_time4 = my_timer4()
# 
# # print("End time is " + str(end_time))
# # print("local end time is " )
# print("Timer 1") 
# print("Started at " + time.strftime("%X", time.localtime(start_time1)))
# print("stopped at " + time.strftime("%X", time.localtime(end_time1)))
#  
# print("Your reaction time was {}".format(end_time1 - start_time1))
# 
# print("Timer 2")
# print("Started at " + time.strftime("%X", time.localtime(start_time2)))
# print("stopped at " + time.strftime("%X", time.localtime(end_time2)))
#  
# print("Your reaction time was {}".format(end_time2 - start_time2))
# print("Timer 3")
# 
# print("Started at " + time.strftime("%X", time.localtime(start_time3)))
# print("stopped at " + time.strftime("%X", time.localtime(end_time3)))
#  
# print("Your reaction time was {}".format(end_time3 -start_time3))
# 
# print("Timer 4")
# print("Started at " + time.strftime("%X", time.localtime(start_time4)))
# print("stopped at " + time.strftime("%X", time.localtime(end_time4)))
#  
# print("Your reaction time was {}".format(end_time4 - start_time4))


import time
print("Time():\t\t", time.get_clock_info('time'))
print("perf_counter:\t", time.get_clock_info('perf_counter'))
print("monotonic:\t", time.get_clock_info('monotonic'))
print('process_time():\t', time.get_clock_info('process_time'))