import random
import string


def make_cell_number(num_cell_numbers):
    num_list = []   
    ph_num = []
    for _ in range(num_cell_numbers):
        ph_num = []
        ph_num.append(random.sample(range(10),10))
        flat = [item for sublist in ph_num for item in sublist]
        ph_num_join = int(''.join(map(str,flat)))
        num_list.append(ph_num_join)

    return num_list

def make_message(num_messages,message_length):
    res_list = []
    for _ in range(num_messages):
        message_str = ''.join(random.choice(string.ascii_letters) for i in range(message_length))
        res_list.append(message_str)
    return(res_list)

    
def produce(num_of_recievers=1000, message_len=100):
    num_list = make_cell_number(num_of_recievers)
    mess_list = make_message(num_of_recievers,message_len)
    return(zip(num_list,mess_list))



