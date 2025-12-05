# import sys
# sys.path.append(r"C:\Users\Saptadeep\Desktop\Python")
# import kaal
import random
import time

rand=[]
for i in range (1,101):
    rand.append(i)

for a in range(1,21):
    time.sleep(1)
    print(random.choice(rand))
    # kaal.loading()


# import os

# while True:
#     name = input("Enter your name: ")
#     # Clear the terminal screen
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("Hello", name)
