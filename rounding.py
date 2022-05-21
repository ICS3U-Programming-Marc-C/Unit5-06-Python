#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program rounds decimals


# Defining the function that rounds up the decimal
def round_decimal(decimal_num, decimal_place):
    decimal_num[0] = decimal_num[0] * (10**decimal_place)
    decimal_num[0] += 0.5
    decimal_num[0] = int(decimal_var[0])
    decimal_num[0] = decimal_num[0] / (10**decimal_place)


if __name__ == "__main__":
    # Getting the user input
    user_decimal_num = input("Enter a decimal number: ")
    user_decimal_place = input("Enter the amount of decimal places: ")

    try:
        # Converting to integer and float
        user_decimal_num_float = float(user_decimal_num)
        user_decimal_place_int = int(user_decimal_place)
        # Adding number to list in order to pass it by reference
        decimal_var = []
        decimal_var.append(user_decimal_num_float)

        # Calling out the function
        round_decimal(decimal_var, user_decimal_place_int)

        print("")
        # Printing out the result
        print("The rounded number is {}".format(decimal_var[0]))

    except:
        # Exception message
        print("Invalid input. Please input a proper decimal and a proper number.")
