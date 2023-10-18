from producer import produce
import numpy as np
import math
from itertools import islice
import time
import concurrent.futures

def per_sender(inner_list):
    sleep_time = inner_list
    time.sleep(sleep_time)


def send(num_senders, num_recievers, mess_len,mean_time_secs,std_time, fail_rate):
    pool = concurrent.futures.ThreadPoolExecutor()
    chunks =[]
    prod = produce(num_recievers,mess_len)
    unzip_prod = list(prod)
    without_dropped_sms = unzip_prod[0:(len(unzip_prod) - math.ceil((len(unzip_prod)*fail_rate)))]
    num_per_sender = [len(without_dropped_sms) // num_senders + (1 if x < len(without_dropped_sms) % num_senders else 0)  for x in range (num_senders)]
    time_dist = np.random.normal(mean_time_secs, std_time,len(without_dropped_sms))   


    new_zip = zip(without_dropped_sms,time_dist)
    it = iter(list(new_zip))
    chunks.append([list(islice(it, 0, j)) for j in num_per_sender])
    for j in range(len(chunks[0])):
        for i in range(len(chunks[0][j])):
            print(chunks[0][j][i][1])
            pool.submit(per_sender(chunks[0][j][i][1]))
    pool.shutdown(wait=True)
 
    print("All senders completed")


print(send(2,5,10,3,0.5,0))

    



