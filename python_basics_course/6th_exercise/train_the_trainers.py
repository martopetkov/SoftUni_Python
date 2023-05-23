jury = int(input())
presentation_name = input()
all_marks_sum = 0
marks_counter = 0

while presentation_name != 'Finish':
    sum_marks = 0
    average_mark = 0

    for i in range(jury):
        sum_marks += float(input())
        marks_counter += 1

    average_mark = sum_marks / jury

    print(f'{presentation_name} - {average_mark:.2f}.')
    presentation_name = input()

    all_marks_sum += sum_marks

total_average_mark = all_marks_sum / marks_counter

print(f"Student's final assessment is {total_average_mark:.2f}.")