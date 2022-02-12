import matplotlib.pyplot as plt
import random
import time
from tqdm import tqdm

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







sample_count = 5000
max_amount_numbers = 150



time_list = []
for nu in tqdm(range(1, max_amount_numbers)):
    time1 = time.time()
    for sample in range(sample_count):
        radix(randomList(nu))
    time2 = time.time()

    time_difference = (time2 - time1)/sample_count
    time_list.append(time_difference)




    plt.plot(range(len(time_list)), time_list,  "b.")
    plt.draw()
    plt.pause(0.0001)
    plt.clf()

plt.plot(range(max_amount_numbers-1), time_list,  "b.")
plt.show()