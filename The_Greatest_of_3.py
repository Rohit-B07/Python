a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
print("The Greatest number is : ")
if (a>=b) and (a>=c):
        print(a)
elif (b>=a) and (b>=c):
        print(b)
else:
        print(c)