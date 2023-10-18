from producer import produce
from progress1 import progress_bar
import numpy as np
import math
from itertools import islice
import concurrent.futures
import random

def per_sender(i,sleep_time,num_per_sender,dropped):
    progress_bar(i,sleep_time,num_per_sender,dropped)


def send(num_senders, num_recievers, mess_len,mean_time_secs,std_time, fail_rate):
    pool = concurrent.futures.ThreadPoolExecutor()
    chunks =[]
    dropped_sms = []
    dropped = 0
    prod = produce(num_recievers,mess_len)
    unzip_prod = list(prod) #turn zip object into list

    failed_sms = math.ceil((len(unzip_prod))*fail_rate) #calculate the number of failed messages
    without_dropped_sms = unzip_prod.copy() #without dropped means the list is all except the dropped messages
    for _ in range(failed_sms):
        random_element = random.choice(without_dropped_sms) 
        dropped_sms.append(random_element)
        without_dropped_sms.remove(random_element)
    # set the number of messages evenly and then take the remainder and split evenly across as many senders as required (less that total number of senders)
    num_per_sender = [len(unzip_prod) // num_senders + (1 if x < len(unzip_prod) % num_senders else 0)  for x in range (num_senders)]
    time_dist = np.random.normal(mean_time_secs, std_time,len(unzip_prod)) #create a time distribution given mean and std dev.  
    #actually split up the messages according to the above message distribution
    new_zip = zip(unzip_prod,time_dist)
    it = iter(list(new_zip))
    chunks.append([list(islice(it, 0, j)) for j in num_per_sender])
    # cleaning up the mess of lists I created...
    for i in range(num_senders):    
        for j in range(len(chunks[0][i])):
            if(chunks[0][i][j][0] in dropped_sms):
                print("SMS dropped")
                dropped += 1
            else:
                pool.submit(per_sender(i,chunks[0][i],num_per_sender, dropped)) #multithreading
                break
    pool.shutdown(wait=True)
 
    print("All senders completed.")





