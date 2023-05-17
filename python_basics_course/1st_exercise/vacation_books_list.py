number_of_pages = int(input())
pages_for_1_hour = int(input())
number_of_days = int(input())
needed_time_in_hours = number_of_pages // pages_for_1_hour
needed_hours_per_day = needed_time_in_hours / number_of_days
print(needed_hours_per_day)