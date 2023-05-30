def data_type(text, num):
    if text == "int":
        return int(num) * 2
    if text == "real":
        result = float(num) * 1.5
        return f"{result:.2f}"
    if text == "string":
        return f"${num}$"



command = input()
number = input()
print(data_type(command, number))