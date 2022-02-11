# Random password generator

import random
import array

pass_len = int(input("Enter the length of password : "))

low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
up_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['@', '#',]

all = low_case + up_case + digit

rand_low = random.choice(low_case)
rand_up = random.choice(up_case)
rand_digit = random.choice(digit)
rand_symbol = random.choice(symbol)

temp_pass = rand_low + rand_up + rand_digit + rand_symbol

for i in range(pass_len - 4):
    temp_pass = temp_pass + random.choice(all)
    temp_pass_l1 = array.array('u', temp_pass)
    random.shuffle(temp_pass_l1)

password = ""

for x in temp_pass_l1:
        password = password + x

print(password)

