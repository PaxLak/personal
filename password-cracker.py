# password-cracker.py

#imports
import random
import string
from os import system, name
import time

#clear terminal
system('cls' if name == 'nt' else 'clear')

#setup
password_length = int(input("Enter desired password length: "))

printable = string.printable[:-6]  # remove whitespace characters for simplicity
correct_password = "".join(random.choices(printable, k=password_length))
print(f"correct password is: \033[1;32m{correct_password}\033[0m\n")


#main loop
found = False
i = 0
start_time = time.time()
print(f"Trying password: " + " " * password_length, end='')
while not found:
    attempt = ''.join(random.Random(i).choices(printable, k=password_length))
    print("\b"*password_length + f"\033[1;34m{attempt}\033[0m", end='')
    if attempt == correct_password:
        found = True
        elapsed_time = time.time() - start_time
        print(f"\n\ntime taken: \033[1;32m{elapsed_time:.2f}s\033[0m")
        print(f"total attempts: \033[1;32m{i}\033[0m")
        print(f"Average attempts per second: \033[1;31m{i/elapsed_time:.2f}\033[0m")
    i += 1

