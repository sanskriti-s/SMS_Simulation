from progress.bar import Bar
from time import sleep


def progress_bar(j,sleep_time,num_recievers_per_sender,dropped):
    with Bar('Sender '+str(j)+' SMS sent', max=num_recievers_per_sender[j]) as bar:
        for i in range(num_recievers_per_sender[j]):
            print('\nWait time: '+str(sleep_time[i][1]))
            print('\nNum of dropped sms: '+str(dropped))
            sleep(sleep_time[i][1])
            bar.next()

