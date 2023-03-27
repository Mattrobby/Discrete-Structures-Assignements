import math
import time

def fibonacci_recursive(n):
    if n == 0:
        return n
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_formula(n):
    answer = (1 / math.sqrt(5)) * (((1 + math.sqrt(5))/ 2) ** n - ((1 - math.sqrt(5))/ 2) ** n)
    return int(answer)


while True:
    try: 
        n = int(input('==> Enter the value of n you want to calculate the Fibonacci Sequence to: '))
        
        if n < 0:
            raise Exception("Input less than 0")
        break

    except:
        print('Please enter a valid integer')
        print()
formula_time_start = time.time()
formula = fibonacci_formula(n)
formula_time_end = time.time()

formula_time = formula_time_end - formula_time_start
print(f'Fibonacci Formula:   {formula}   Time: {formula_time}')

recursive_time_start = time.time()
recursive = fibonacci_recursive(n)
recursive_time_end = time.time()

recursive_time = recursive_time_end - formula_time_start
print(f'Fibonacci Recursive: {recursive}   Time: {recursive_time}')
