needed_nailon = int(input())
needed_paint = int(input())
needed_razreditel = int(input())
hours = int(input())

total_sum = ((needed_nailon + 2) * 1.50) + ((needed_paint + needed_paint * 0.10) * 14.50) + (needed_razreditel * 5) + 0.40
money_for_maystors = (total_sum * 0.30) * hours
final_sum = total_sum + money_for_maystors
print(final_sum)