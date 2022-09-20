#Practice code for 7.28
#add timers
import time
start_time1 = time.time()
num: []
for num in range(1,10000):
    if num % 5 == 0 and num % 25 == 0:
        # print(num)
        end_time1 = time.time()
        total_time1 = start_time1-end_time1


#x for x in interable =

start_time2 = time.time()
new_list = [num for num in range(1,10000) if num % 5 == 0 and num % 25 == 0]
#print(new_list)
end_time2 = time.time()
total_time2 = start_time2 - end_time2
print('The total time was for the for loop was:', total_time1, 'seconds.')
print('The total time for list comprehension was:', total_time2, 'seconds.')