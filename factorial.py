while(1):
    
    def factorial(n):
        """Factorial using recursion"""
        if (n==1 or n==0):
            return 1
        else:
            return n*factorial(n-1)      #Calling the function in the defination(Recursion)  
    
    n=int(input("Enter a number to find out Factorial: "))
    print(factorial(n))

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
       
        return fib(n-1)+fib(n-2)
        
