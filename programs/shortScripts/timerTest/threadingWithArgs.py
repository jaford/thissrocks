from time import sleep, perf_counter
from threading import Thread
import decimal


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')


start_time = perf_counter()

# create and start 10 threads
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()


totalTime = end_time - start_time 
totalTime = decimal.Decimal(totalTime)
totalTime = totalTime.quantize(decimal.Decimal('0.00')) # Converted the float to a deci and rounded to the nearest hundreth! 

print('It took {} second(s) to complete.'.format(totalTime))

