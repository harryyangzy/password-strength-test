
"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Harry Yang
Student ID: hyang746
File created: October 19, 2024
******************************
This file has a function used to generate a random password at
a length given by the input from the user. The password consists
of random characters from a string of characters.
"""

import random #python random library

# letter bank for possible password characters
ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"

#function that takes password length and generates password
#with random characters from letter bank
def generate_password(length):
    password = ""
    # loop chooses random character and adds it to password length
    for i in range (length):
        password = password + random.choice(ALL_CHARS)
    return password

