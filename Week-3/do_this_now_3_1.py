"""
Do this now from (week 3)
Write a program that asks the user for their age and then prints whether it is odd or even.
The program should not crash if the user enters a non-number (i.e. use exception handling)
The program should not allow an invalid age number
Re-prompt until a valid number is entered
"""


def main():
    is_valid_input = False
    while not is_valid_input:
        try:
            age = int(input("Enter an age:"))
            if age < 0 or age > 200:
                print("Age must be between 0 and 200")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid integer")

    if is_even(age) == 0:
        print("This is even number")
    else:
        print("This is odd number")


def is_even(number):
    if number % 2 == 0:
        return True


main()
