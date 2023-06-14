employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students = int(input())

answers_per_hour = employee_one + employee_two + employee_three
hours = 0

while students > 0:
    students -= answers_per_hour
    hours += 1

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")