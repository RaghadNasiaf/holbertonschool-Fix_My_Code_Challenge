#!/usr/bin/python3
import sys


def fizzbuzz(n):
    """Print numbers from 1 to n with FizzBuzz rules"""
    tmp_result = []

    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))

    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            fizzbuzz(n)
        except ValueError:
            print("Please provide a valid integer")
    else:
        print("Usage: ./0-fizzbuzz.py <number>")

