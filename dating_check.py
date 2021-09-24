#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user input their age to see if they are able to date the grandchild


def main():
    # this tells the user if they can date the grandchild

    # input
    age_check = input("Please enter your age: ")

    # process & output
    try:
        integer_as_number = int(age_check)

        if integer_as_number >= 25 and integer_as_number <= 40:
            print("You are accepted to date my grandchild!")

        else:
            print("You can not date my grandchild!")

    except Exception:
        print("This is not a number!")

    finally:
        print("Thank you for checking your age!")
        print("\nDone.")


if __name__ == "__main__":
    main()
