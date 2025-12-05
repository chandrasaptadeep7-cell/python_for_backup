def is_prime(n):
    if n==2 or n==3:
        return True
    
    elif n==0 or n==1:
        return False
    
    elif n%2==0 :
        return False
    
   
    i=3
    while i*i <= n:
        if n%i==0:
            return False
        i=i+2
    return True

def find_prime_in_range(a,z):
    prime=[ ]
    n=a
    while n<=z:
        if is_prime(n):
            prime.append(n)
        n=1+n
    return prime


print(find_prime_in_range(1,1000))

