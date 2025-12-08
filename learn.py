import time
import random


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("[log] is running")
        result = func(*args, **kwargs)
        print("[log] is finished")
        end_time = time.time()
        elasped_time = end_time - start_time
        print(f"{func.__name__} took {elasped_time} seconds to run")
        return result

    return wrapper


@time_it
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(calculate_sum(1000000))


def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 3
        for i in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"{i+1} failed failed: {e}")
                time.sleep(1)
        print("All attempts failed")

    return wrapper


@retry
def sometimes_fails():
    if random.random() < 0.7:  # 70% chance to fail
        raise ValueError("Random failure!")
    return "Success!"


print(sometimes_fails())


def validate_integers(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            print("must be an integer")
            return
        return func(*args, **kwargs)

    return wrapper


@validate_integers
def add(a, b):
    return a + b


print(add(5, 3))
