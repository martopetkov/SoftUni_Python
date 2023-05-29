numbers = int(input())


for i in range(numbers):
    new_num = int(input())
    if new_num % 2 != 0:
        print(f"{new_num} is odd!")
        break
else:
    print("All numbers are even.")
