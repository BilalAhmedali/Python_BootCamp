
while True:
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    operation = input("Please choice one of math operation above to calculate ")

    numOne = int(input("Enter first number: "))
    numTwo = int(input("Enter second number: "))

    if operation.title == "Addition" or operation == "1":
        Addition = lambda x,y:x+y
        print(Addition(numOne,numTwo))
    
    elif operation.title() == "Subtraction" or operation == '2':
        Subtraction = lambda x,y : x-y
        print(Subtraction(numOne,numTwo))

    elif operation.title() == "Multiplication" or operation == "3":
        Multiplication = lambda x,y:x*y
        print(Multiplication(numOne,numTwo))
    
    elif operation.title() == "Division" or operation == '4':
        Division = lambda x,y:x/y
        print(Division(numOne,numTwo))
    else:
        print("Sorry operation not in a list")

    calculation = input("Do you wish to calculation agian or quite  (yes or no)")
    if calculation.lower() == "no":
        break

    
