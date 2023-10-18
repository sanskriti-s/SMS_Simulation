from progress.bar import Bar
from time import sleep


def progress_bar(num_senders,sleep_time,num_recievers_per_sender):
    for j in range(num_senders):
        with Bar('Sender '+str(j)+' Packets sent', max=num_recievers_per_sender[j]) as bar:
            for i in range(num_recievers_per_sender[j]):
                print('\n'+str(sleep_time[j][i][1]))
                sleep(sleep_time[j][i][1])
                bar.next()

