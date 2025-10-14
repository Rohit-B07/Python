a = int(input("Enter the First number :"))
b = int(input("Enter the Second number :"))

A = a+b
B = a-b
C = a*b
D = a//b
E = a**2

c = int(input("Select the operation 1, 2, 3, 4, 5: "))

if c == 1:
    print(A)
elif c == 2:
    print(B)
elif c == 3 :
    print(C)
elif c == 4:
    print(D)
elif c == 5:
    print(E)
else :
    print("Invalid Input")

