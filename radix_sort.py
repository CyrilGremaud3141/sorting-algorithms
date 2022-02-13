import matplotlib.pyplot as plt
import random
import time
from tqdm import tqdm

import multiprocessing
import os
num_processes = 1
if num_processes > os.cpu_count():
    num_processes = os.cpu_count()
print(num_processes)

def randomList(n):
    l = list(range(n))
    random.shuffle(l)
    return l


def radix(lis):
    stellen = len(str(max(lis)))
    lis = [x.zfill(stellen) for x in list(map(str, lis))]
    
    for stelle in range(stellen):
        new_lis = []
        for digit in range(10):
            dig = str(digit)
            for element in lis:
                if element[-(stelle+1)] == dig:
                    new_lis.append(element)
        lis = new_lis




    return lis




def sample(nu):
    for sample in range(sample_count):
        radix(randomList(nu))


sample_count = 1000
max_amount_numbers = 3000

processes = []

time_list = []

for pr in range(num_processes):
    p = multiprocessing.Process(target=sample, args=[pr+1])
    p.start()
    processes.append((p, time.time()))

for nu in tqdm(range(num_processes+1, max_amount_numbers)):

    processes[0][0].join()
    time1 = processes[0][1]
    time2 = time.time()

    time_difference = (time2 - time1)/sample_count
    time_list.append(time_difference)


    plt.plot(range(len(time_list)), time_list,  "b.")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

    processes.pop(0)
    p = multiprocessing.Process(target=sample, args=[nu])
    p.start()
    processes.append((p, time.time()))


for process in processes:
    process[0].join()
    time1 = process[1]
    time2 = time.time()

    time_difference = (time2 - time1)/sample_count
    time_list.append(time_difference)


    plt.plot(range(len(time_list)), time_list,  "b.")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

    

plt.plot(range(max_amount_numbers-1), time_list,  "b.")
plt.show()