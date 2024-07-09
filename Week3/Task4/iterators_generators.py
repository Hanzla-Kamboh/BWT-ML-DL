# Iterators and Generators - iterators_generators.py

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        else:
            self.start -= 1
            return self.start + 1

def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

import random

def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)

# Example usage:
try:
    countdown = Countdown(5)
    for number in countdown:
        print(number)

    for fib in fibonacci_generator(100):
        print(fib)

    for rnd in random_number_generator(1, 100, 10):
        print(rnd)
except Exception as e:
    print(f"An error occurred: {e}")
