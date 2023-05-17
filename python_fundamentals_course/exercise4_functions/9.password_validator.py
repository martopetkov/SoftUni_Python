import re


def validator(text):
    if len(text) < 6 or len(text) > 10:
        print("Password must be between 6 and 10 character")
    for i in range(len(text)):
        if text in range(ord("0"), ord("Z") + 1):
            print("Password must consist only of letters and digits")


password = input()
validator(password)


