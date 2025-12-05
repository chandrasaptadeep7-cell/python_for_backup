

import sys
sys.path.append(r"C:\Users\Saptadeep\Desktop\Python")
import kaal

def leapyear(y):
    if y%4==0 and y%100!=0 or y%400==0:         # Base logic
        return True
    else:
        return False
    
list_y=[]                                        # lIST DECLARATION

for y in range (2000,2100):                          # Range of the year
    if leapyear(y):                               #If true the yeat will be added in the list
        list_y.append(y)
    

kaal.delay(2)
print(list_y)                                         #Fuction call
print(f"Total {len(list_y)} years are there.")
    