
"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Harry Yang
Student ID: hyang746
File created: October 19, 2024
******************************
This file has a function which prompts the user for a password until
the password reaches a minimum strength determined by the argument accepted
when the function is called. If the user chooses, they may also prompt
the function to generate a random password which may or may not reach
the minimum strength.
"""

# import python files from folder
from password import *
from generate import *

# function which prompts user to create a password to minimum strength
# or will create a password to the minimum strength for the user
def process_password(min_strength):
    strength = -1 # strength measure variable
    while strength < min_strength:
        password = input("Type in a new password or type X for a randomly generated password: ")
        # if user types 'x' or 'X' program will generate password for user
        if password.upper() == 'X':
            password = generate_password(15)
            print("Your password:", password)
        else:
            print("You entered:", password)
        # measures strength using strength function
        strength = password_strength(password)
        print("Your password has a strength of", strength)
        # compares strength to minimum strength and creates output message
        if strength < min_strength:
            print("Your password is not strong enough. Please create a new password that is stronger.")
        else:
            print("Your password is strong enough! Thank you.")


