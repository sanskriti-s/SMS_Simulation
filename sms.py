from sender import send
import sys 

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Enter the following configurations: \nnum_senders(int) \nnum_recievers(int) \nmess_len(int) \nmean_time(float) \nstd_time(float) \nfail_rate(float <= 1)")
        exit(0)
    
    program = sys.argv[0] 
    num_senders = int(sys.argv[1])
    num_recievers = int(sys.argv[2]) 
    mess_len = int(sys.argv[3])
    mean_time = float(sys.argv[4])
    std_time = float(sys.argv[5])
    fail_rate = float(sys.argv[6])
    send(num_senders,num_recievers,mess_len,mean_time,std_time,fail_rate)
