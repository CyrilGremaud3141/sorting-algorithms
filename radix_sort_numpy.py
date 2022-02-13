import matplotlib.pyplot as plt
import random
import time
from tqdm import tqdm
import numpy as np 
import math


def randomList(n):
    l = np.arange(n)
    np.random.shuffle(l)
    return l

def radix(lis):
    max_number = np.nanmax(lis)
    if max_number == 0:
        return lis
    stellen = int(math.log10(max_number)) + 1
    length = lis.shape[0]
    

    
    for stelle in np.arange(stellen):
        new_lis = np.zeros(shape=length, dtype=np.int64)
        # counting sort
        count_lis = np.zeros(10)
        for element in lis:
            digit = int((element // (10 ** stelle) % 10))
            count_lis[digit] += 1

        for c in range(1,10):
            count_lis[c] = count_lis[c] + count_lis[c-1]

        for element in lis:
            digit = int((element // (10 ** stelle) % 10))
            new_lis[int(count_lis[digit]-1)] = element
            count_lis[digit] -= 1

        lis = np.flip(new_lis)





    return np.flip(lis)



def sample(nu):
    for sample in range(sample_count):
        radix(randomList(nu))

sample_count = 1000
max_amount_numbers = 200


time_list = []


for nu in tqdm(range(1, max_amount_numbers)):

    time1 = time.time()
    sample(nu)
    time2 = time.time()

    time_difference = (time2 - time1)/sample_count
    time_list.append(time_difference)


    plt.plot(range(len(time_list)), time_list,  "b.")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()


plt.plot(range(max_amount_numbers-1), time_list,  "b.")
plt.show()