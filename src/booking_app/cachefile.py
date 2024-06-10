from time import sleep
from functools import lru_cache


# Task 1
CACHE_FACTORIAL = {}

def factoria(N):
    if N in CACHE_FACTORIAL:
        return CACHE_FACTORIAL[N]
    else:
        sleep(3)
        if N == 0 or N == 1:
            CACHE_FACTORIAL[N] = 1
        else:
            CACHE_FACTORIAL[N] = N * factoria(N - 1)
        return CACHE_FACTORIAL[N]

print(factoria(5))
print(factoria(5))
print(factoria(6))
print(factoria(6))


# Task 2
@lru_cache(None)
def sum_positive(numbers):
    if len(numbers) == 0:
        return 0

    current_number = numbers[0]
    remaining_numbers = tuple(numbers[1:])

    if current_number > 0:
        return current_number + sum_positive(remaining_numbers)
    else:
        return sum_positive(remaining_numbers)


numbers = [1, -2, 3, 4, -5, 6]
print(sum_positive(tuple(numbers)))