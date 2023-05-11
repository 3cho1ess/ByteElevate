import os
import random
import string
import time
from colorama import init, Fore, Style

# initialize colorama module
init()

# welcome message
print(Fore.CYAN + "Welcome to ByteElevate!" + Style.RESET_ALL)
print()
print("This program utilizes advanced algorithms to generate a text file with a precise size in bytes.")
print("You can use this program to benchmark the performance of your storage devices or to create sample data for your software applications.")
print()
print(Fore.YELLOW + "Note: This program is optimized for high performance and may take some time to complete depending on your hardware specifications." + Style.RESET_ALL)
print()

# prompt for file name
filename = input(Fore.CYAN + "What do you want to name the output txt file: " + Style.RESET_ALL)

while not filename:
    print(Fore.RED + "Please enter a valid name." + Style.RESET_ALL)
    print()
    filename = input(Fore.CYAN + "What do you want to name the output txt file: " + Style.RESET_ALL)

print()

# prompt for file size
size = input(Fore.CYAN + "Enter the desired size of the file in bytes: " + Style.RESET_ALL)
while not size.isdigit() or int(size) <= 0:
    print(Fore.RED + "Please enter a valid positive integer for the file size." + Style.RESET_ALL)
    print()
    size = input(Fore.CYAN + "Enter the desired size of the file in bytes: " + Style.RESET_ALL)

print()

# convert size to integer
size = int(size)

# adjust file name extension to .txt
filename = os.path.splitext(filename)[0] + '.txt'

# check if file already exists, prompt for a new name if necessary
while os.path.isfile(filename):
    print(Fore.RED + "File already exists. Please enter a different name." + Style.RESET_ALL)
    print()
    filename = input(Fore.CYAN + "Enter the name of the file: " + Style.RESET_ALL)
    filename = os.path.splitext(filename)[0] + '.txt'

# generate dots animation while the file is being created
dots = [".", " ..", " ..."]
dot_index = 0
print(Fore.YELLOW + f"Making txt '{filename}'" + Style.RESET_ALL, end="", flush=True)

start_time = time.time()

# generate random text data with lowercase, uppercase, numbers, symbols, and null bytes
data = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + '\x00', k=size))

with open(filename, 'wb') as f:
    f.write(data.encode('utf-8'))

# check the size of the file
file_size = os.path.getsize(filename)
print(Fore.GREEN + " Done!" + Style.RESET_ALL)
print()
print(Fore.LIGHTGREEN_EX + f"File size: {file_size} bytes" + Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX + f"Elapsed time: {time.time() - start_time:.4f} seconds" + Style.RESET_ALL)
print()
print(Fore.CYAN + "File created successfully." + Style.RESET_ALL)
print()
input("Press Enter to exit...")

# keep asking for enter key press until the user presses it
while True:
    if input() == "":
        break
