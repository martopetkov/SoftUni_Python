def validator(text):
    is_valid = True
    if len(text) < 6 or len(text) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if not text.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digit_counter = 0
    for ch in text:
        if ch.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    return is_valid


password = input()
is_valid = validator(password)
if is_valid:
    print("Password is valid")


