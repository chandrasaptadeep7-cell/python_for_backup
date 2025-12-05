
while(1):

    import random
    e_list=("Rock", "Paper", "Sessior")        #List declaretion.

    print()
    print("Enter 'R' for Rock")                 # Display the instruction.
    print("Enter 'S' for Sessior ")
    print("Enter 'P' for Paper")
    print(" ")

    choice=input("Enter your choice: ").lower()         
    comp_choice=random.choice(e_list)               #Making the list ranom



    if choice=="r" :                 #
        choice="Rock"
    elif  choice=="s":
        choice="Sessior"
    elif choice=="p" :
        choice="Paper"
    else: 
     print(f"User choice= {choice}, Computer choice={comp_choice}, INVALID INPUT.")
    
    if choice==comp_choice:
      print(f"User choice= {choice}, Computer choice={comp_choice},THE MATCH IS DRAW!")

    elif choice=="Rock":
        if comp_choice=="Sessior":
            print("Sessior smashed by Rock, YOU WIN!")
        else:
            print("Paper covers Rock, COMPUTER WON!")
    
    elif choice=='Paper':
        if comp_choice=="Rock":
            print("Paper cover Rock, YOU WON!")
        else:
            print("Sessior cut Paper,COMPUTER WON!")
    
    elif choice=='Sessior':
        if comp_choice=="Rock":
            print("Rock smashes Sessior, COMPUTER WON!")
        else:
            print("Sessior cuted Papper,YOU WON!")

