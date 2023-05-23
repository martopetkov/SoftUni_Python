name = input()
grades_counter = 0
years_counter = 0
failed_years = 0


while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1

        if failed_years == 2:
            current_failed_year = years_counter + 1
            print(f"{name} has been excluded at {current_failed_year} grade")
            break

        continue

    years_counter += 1
    grades_counter += annual_grade

    if years_counter == 12:
        sum_average = grades_counter / 12
        print(f'{name} graduated. Average grade: {sum_average:.2f}')
        break
