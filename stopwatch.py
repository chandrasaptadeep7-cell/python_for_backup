import sys
sys.path.append(r"C:\Users\Saptadeep\Desktop\Python")


import time
import kaal


t=int(input("Enter the stop time in second: "))

while(t>=0):
    time.sleep(1)
    kaal.clr_screen()  #To clear display or terminal
    print(t)
    t-=1


print("Time is over. ")




# Ideas
"""*Timer  """



