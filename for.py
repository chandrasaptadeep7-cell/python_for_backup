a=(input("Enter a number: "))

try:
    for i in range(1,11):
        print(int(a), "X", i,"=", a*i)
except:
    print("Enter a number, not a character.")


print("//Codes")