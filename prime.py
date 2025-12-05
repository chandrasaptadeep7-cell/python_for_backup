
# Check a number is prime or not
is_prime=[" ",]


def prime(a):
        if a%2==0 or a%3==0:
            print ("Not a prime.")    # Even number will not be prime.

        elif a==0 or a==1:
         print("Not a prime.")
         return False

        elif a==2 or a==3:
         print("Prime.")
            
            

        elif a>=5:
         i=5
         while i<a:
             
                if a%i==0:
                    print("Not a prime.")
                    break
                else:
                    print("Prime.")
                    break


        i+=1




n=int(input("Enter a number: "))
prime(n)