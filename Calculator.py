import sys


# Define Add Function
def add():
    # This Function take n number of numbers and sum of all them
    print("Start entering the number : ")
    number_list = []
    while True:
        user_input = int(
            input("Enter a value (or Press 000 to quit): ")
        )  # Here is the exit from code

        if user_input == 000:
            break

        number_list.append(user_input)  # Adding Number into list

    number_list_sum = sum(number_list)  # Sum of all number in number list
    print(f" The Sum of numbers are : {number_list_sum}")
    restart()  # Calling Restart Function


def sub():
    num1 = int(input("Enter Number 1:  "))
    num2 = int(input("Enter Number 2:  "))
    sub = num1 - num2
    print(f"The Subtraction of {num1} - {num2} = {sub}")
    restart()


def multi():
    num1 = int(input("Enter Number 1:  "))
    num2 = int(input("Enter Number 2:  "))
    multi = num1 * num2
    print(f"The multiplication of {num1} * {num2} = {multi}")
    restart()


def divi():
    num1 = int(input("Enter Number 1:  "))
    num2 = int(input("Enter Number 2:  "))
    qutiento = num1 // num2
    print(f"The qutioent of two Number = {qutiento}")
    restart()


# Define restart function
def restart():
    restart = int(input("Enter 9 for Restart or 99 for exit:  "))
    if restart == 9:
        main()
    elif restart == 99:
        print("Existing from Program")
        sys.exit()
    else:
        print("Invalid input")


# Define Main Function according to the input it works
def main():
    print("______  Welcome To  Calculator ____\n")
    print("--- Press 1 For Addition---\n")
    print("--- Press 2 For Subtraction---\n")
    print("--- Press 3 For Multiplication---\n")
    print("--- Press 4 For Division---\n")

    option = input("Enter your Option:  ")

    if option == "1":
        add()

    elif option == "2":
        sub()

    elif option == "3":
        multi()

    elif option == "4":
        divi()

    else:
        print("Invalid Input")


# This code says that always main function start first
if __name__ == "__main__":
    main()
