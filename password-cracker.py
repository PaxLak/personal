# password-cracker.py

#imports
import random
import string
from os import system, name
import time

#clear terminal
system('cls' if name == 'nt' else 'clear')

#get list of excepted characters
chars = string.printable[:-6]  #whitespace removed


#setup
if input("Generate random password? [Y/n]: ").strip().lower() != "n":
    correct_password = "".join(random.choices(chars, k=int(input("Length generated of password: "))))    #generate random password
else:
    correct_password = input("Enter password: ").strip()

input("Enter to continue\n")  #pause
system('cls' if name == 'nt' else 'clear')

print(f"Password is: \033[1;32m{correct_password}\033[0m")    #print correct password

#main loop setup
found = False
i = 0
start_time = time.time()
print(f"Trying password: " + "#" * len(correct_password), end='')

#main loop
while not found:
    attempt = ''.join(random.Random(i).choices(chars, k=len(correct_password)))   #generate attempt

    print("\b"*len(correct_password) + f"\033[1;34m{attempt}\033[0m", end='') #print attempt

    if attempt == correct_password:
        found = True
        elapsed_time = time.time() - start_time
        print(f"\n\ntime taken: \033[1;32m{elapsed_time:.2f}s\033[0m")
        print(f"total attempts: \033[1;32m{i}\033[0m")
        print(f"Average attempts per second: \033[1;32m{i/elapsed_time:.2f}\033[0m")

    i += 1

