

student_ticket = 0
standard_ticket = 0
kid_ticket = 0

movie_name = input()
while movie_name != "Finish":
    free_seats = int(input())
    sold_tickets = 0

    while free_seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break

        free_seats -= 1
        sold_tickets += 1

        if ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1

    percent_sold_tickets = (sold_tickets / (free_seats + sold_tickets )) * 100
    print(f'{movie_name} - {percent_sold_tickets:.2f}% full.')

    movie_name = input()

total_tickets = student_ticket + standard_ticket + kid_ticket
print(f'Total tickets: {total_tickets}')
print(f'{student_ticket / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_ticket / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_ticket / total_tickets * 100:.2f}% kids tickets.')