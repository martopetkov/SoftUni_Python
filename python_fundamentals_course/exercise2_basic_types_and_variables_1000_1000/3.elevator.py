num_ppl = int(input())
capacity = int(input())
course_count = 0

while num_ppl > 0:
    num_ppl -= capacity
    course_count += 1

print(course_count)



# втори начин

from math import ceil
num_ppl = int(input())
capacity = int(input())

print(ceil(num_ppl / capacity))