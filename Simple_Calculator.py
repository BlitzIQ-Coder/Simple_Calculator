num1 = float(input("Enter 1st number to Calculate: "))
num2 = float(input("Enter 2nd number to Calculate: "))
print("CALCULATOR MENU:\n1. Sum\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
while True:
    user_choice = int(input("Choose the option you want me to do: "))

    if user_choice == 1:
        output = num1 + num2
        print("Total = " + str(output))
    elif user_choice == 2:
        output = num1 - num2
        print("Total = " + str(output))
    elif user_choice == 3:
        output = num1 * num2
        print("Total = " + str(output))
    elif user_choice == 4:
        if (num2 != 0 and num1 != 0):
            quotient = num1 / num2
            remainder = num1 % num2
            print("Quotient = " + str(quotient) + " | Remainder = " + str(remainder))
        else:
            print("Error: Division by zero is not allowed.")
    elif user_choice == 5:
        print("Exiting the TOOL")
        break
    else:
        print("Invalid choice. Please select a valid option from the menu.")

#If You Need GUI you can use Tkinter