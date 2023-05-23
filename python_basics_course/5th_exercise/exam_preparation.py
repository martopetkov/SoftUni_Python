broi_nezadovolitelni_ocenki = int(input())

failed_times = 0
number_of_solved_problems = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < broi_nezadovolitelni_ocenki:
    zadacha = input()
    if zadacha == 'Enough':
        has_failed = False
        break
    ocenka = int(input())

    grades_sum += ocenka
    number_of_solved_problems += 1
    last_problem = zadacha

    if ocenka <= 4:
        failed_times +=1


average_score = grades_sum / number_of_solved_problems

if has_failed:
    print(f'You need a break, {broi_nezadovolitelni_ocenki} poor grades.')
else:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_of_solved_problems}')
    print(f'Last problem: {last_problem}')


