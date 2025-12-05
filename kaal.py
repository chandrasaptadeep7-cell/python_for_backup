import os

def delay(sec):
    for i in range(0,sec):
        x=2
        y=2 
        for i in range(1,10000):
            for a in range(1,2500):
                ab=(x+y)

def loading(msg):             
     delay(1)
     print(msg, end=" ")
     for i in range(1,6):
        print(".",end=" ")
        delay(1)


def clr_screen():
    os.system("cls" if os.name =="nt" else "clear")