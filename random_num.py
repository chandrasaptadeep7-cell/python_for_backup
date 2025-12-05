while(1):
      import random
      choice=[1,]
      for i in range (2,1000):
            choice.append(i)
            i+=1

      list_1=random.choice(choice)
      a=input("Enter 'strt' to start & 'end' to stop: ").lower()

      if (a=="strt"):
            print("Random number is ",list_1)

      elif (a=='end'):
            break

