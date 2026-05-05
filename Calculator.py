
# Basic Arithmatic Problem Solving Calculator

print("\n\t\t\t------ Basic Calculator ------\n")

while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


    user_choice = input("\nEnter Your Choice: ")

    if user_choice == "5":
        print("\nExit The Calculator!")
        print("Thanks For Using!")
        print("------------------------\n")
        break


    if user_choice not in ("1","2","3","4"):
        print("You Entered A Not Existing Choice!")
        continue
        
    
    print("------------------------------------\n")
    num1 = float(input("Enter Your First Number:"))
    num2  = float(input("Enter Your Second Number:"))


    if user_choice == "1":
        print(f"({num1} + {num2}) = {num1+num2}\n")

    elif user_choice == "2":
        print(f"({num1} - {num2}) = {num1-num2}\n")

    elif user_choice == "3":
        print(f"({num1} x {num2}) = {num1*num2}\n")

    elif user_choice == "4":
        if num2 != 0:
            print(f"({num1} / {num2}) = {num1/num2}\n")
        else:
            print("Cannot divide by zero!\n")