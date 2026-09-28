print("program starting")
print("insert two integers")
Numone = int(input("Enter the first integer: "))
Numtwo = int(input("Enter the second integer: "))
print("Comparing the inserted integers:")
if (Numone == Numtwo):
    print("The two integers are equal.")
elif (Numone > Numtwo):    
    print("The first integer is greater than the second integer.")
else:
    print("The first integer is less than the second integer.")
    print("program ending")