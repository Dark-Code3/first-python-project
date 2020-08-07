print("Welcome")
Number1 = input("What is your first number \n")
Number2 = input("What is your secound number \n")
Operation = input("What operation would you like to do?  (Example: + - x / ) \n")

Number1 = int(Number1)
Number2 = int(Number2)
print("Your answer is:")

if(Operation == "+"):
    print(Number1 + Number2)
if(Operation == "-"):
    print(Number1 - Number2)
if(Operation == "x"):
    print(Number1 * Number2)
if(Operation == "/"):
    print(Number1 / Number2)

print()

Number1 = str(Number1)
Number2 = str(Number2)

print(Number1 + Operation + Number2)
