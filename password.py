
"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Harry Yang
Student ID: hyang746
File created: October 19, 2024
******************************
This file is used to count the number of character groups and to
determine a password strength. The password strength is dependent on
the length of the password, the function returns a strength of the
password from 0-5.
"""

# use global variables to define character groups
LOWERCASE_GROUP = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_GROUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS_GROUP = "0123456789"
SYMBOLS_GROUP = "!@#$%^&*/?-+=,.|~"

INVALID_GROUP = ["\t", "\n", " "]

# use function to count the number of groups in a string
def count_groups(pwd):
    # use boolean to track whether character exists in group
    group_one = False
    group_two = False
    group_three = False
    group_four = False

    # use for loop to iterate through and see if character belongs in String groups
    for i in range (len(pwd)):
        if pwd[i] in LOWERCASE_GROUP:
            group_one = True
        elif pwd[i] in UPPERCASE_GROUP:
            group_two = True
        elif pwd[i] in DIGITS_GROUP:
            group_three = True
        elif pwd[i] in SYMBOLS_GROUP:
            group_four = True
    #add up number of groups
    return int(group_one) + int(group_two) + int(group_three) + int(group_four)

# use function to determine strength of password depending on string length
def password_strength(pwd):
    num = count_groups(pwd)

    #check for invalid characters
    for i in range (len(INVALID_GROUP)):
        if INVALID_GROUP[i] in pwd:
            return 0

    if len(pwd) < 5:
        return 0
    elif 5 <= len(pwd) <= 8:
        if num <= 1:
            return 1
        elif 2 <= num <= 3:
            return 2
        elif num > 3:
            return 3
    elif 9 <= len(pwd) <= 12:
        if num <= 1:
            return 2
        elif 2 <= num <= 3:
            return 3
        elif num > 3:
            return 4
    elif len(pwd) > 12:
        if num <= 1:
            return 3
        elif 2 <= num <= 3:
            return 4
        elif num > 3:
            return 5
