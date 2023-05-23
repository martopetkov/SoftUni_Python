steps = 0
goal_steps = 10000

while steps < goal_steps:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        steps += steps_to_home
        break
    steps += int(command)


diff = abs(goal_steps - steps)

if steps >= goal_steps:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
     print(f'{diff} more steps to reach goal.')


