a = int(input("Enter the Year : "))

if (a % 4 == 0) & (a % 100 != 0):
     print("Leap Year")
elif (a % 400 == 0):
     print("Leap Year")
else:
     print("Not a Leap Year") 