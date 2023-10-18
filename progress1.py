from progress.bar import Bar
from time import sleep


def progress_bar(num_senders,sleep_time,num_recievers_per_sender,dropped):
    total_time = 0
    count = 0
    with Bar('Sender '+str(num_senders)+' SMS sent', max=num_recievers_per_sender[num_senders]) as bar:
        for i in range(num_recievers_per_sender[num_senders]):
            total_time +=sleep_time[i][1]
            count += 1
            mean_time = total_time/count
            print('\nAverage wait time: '+str(mean_time))
            print('\nNum of dropped sms: '+str(dropped))
            sleep(sleep_time[i][1]) #create delay
            bar.next()

