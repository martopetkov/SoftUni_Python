obem = int(input())
debit_traba_1 = int(input())
debit_traba_2 = int(input())
chasove = float(input())

first_pipe = debit_traba_1 * chasove
second_pipe = debit_traba_2 * chasove
total_through_pipe = first_pipe + second_pipe

fist_pipe_in_procent = (first_pipe * 100) / total_through_pipe
second_pipe_in_procent = (second_pipe * 100) / total_through_pipe
total_pool_in_procent = (total_through_pipe * 100) / obem

diff = abs(total_through_pipe - obem)
if obem >= total_through_pipe:
   print(f'The pool is {total_pool_in_procent:.2f}% full. Pipe 1: {fist_pipe_in_procent:.2f}%. Pipe 2: {second_pipe_in_procent:.2f}%.')

else:
   print(f'For {chasove:.2f} hours the pool overflows with {diff:.2f} liters.')