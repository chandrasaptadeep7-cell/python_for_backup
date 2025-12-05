
import sys
sys.path.append(r"C:\Users\Saptadeep\Desktop\Python")
import os
import kaal
def title():
    print()
    print("Enter 1. for  add a new contact.")
    print("Enter 2. for show the number of a person. ")
    print("Enter 3. for show the person of a number. ")
    print("Enter 4. to Show the contact list.")
    print()

def delay():
    x=2
    y=2
    ab=0
    for i in range(1,10000):
        for a in range(1,2000):
              ab=x+y


phone={  #Keys   :   Values
        "Saptadeep": 9007716434,
        "Pushpi": 7439101254,
        "Sayan": 111111111,
        "Biswa": 95142367,
        "Deep": 987410255,
        "Tenida": 9475236814,
    }

while(1):
     
    title() 
    choice=int(input("Enter your choice: "))
    print()
    if choice==1:
        person=input("Enter the person's name:  ")
        num=int(input("Enter the phone number:"))
        phone.update({person : num})
        
        print(f"{person}'s number is added")
        kaal.delay(3)

    elif choice==4:
        print("_________________")
        print("|   CONTACTS    |")
        print("-----------------")

        for key in phone.keys():
            print(f"{key} --> {phone[key]}")

    elif choice==2:
        person=input("Enter the person's name: ")
        print(phone.get(person))


    elif choice ==3:
        num =int (input("Enter the phone number: "))
        delay()
        try:
            for name,n in phone.items():
                if n==num:
                    
                    print(name)
        
        except:
            print("""You have entered a character,
                  Please enter numbers.""")

    else:
        print("Please enter in between 1-4.")
    
    os.system('cls' if os.name=='nt' else "clear")


