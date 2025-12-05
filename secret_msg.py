import random



msg=input("Enter your message: ")
rdm="abcdefghijklmnopqrstuvwxyz"

if len(msg)==2:
    i=1
    while i>=0:
        print(msg[i], end="")
        i=i-1
        
elif len(msg)==3:
    a=["",]
    rdm="abcdefghijklmnopqrstuvwxyz"
    for i in range(1,25):
        a.append(i)

    for b in range(0,3):
        encode=int(random.choice(a))
        print(rdm[encode],end="")

    print(msg[1],end="")
    print(msg[2],end="")
    print(msg[0],end="")

    for b in range(0,3):
        encode=int(random.choice(a))
        print(rdm[encode],end="")

    
elif len(msg)>3:
    i=(len(msg)-1)
    while i>=0:
        print(msg[i],end="")
        i=i-1