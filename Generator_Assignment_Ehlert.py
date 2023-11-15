"""
Program Name: Generator_Assignment_Ehlert.py
Author: Tony Ehlert
Date: 11/15/2023

Program Description: This program uses a generator that outputs Fibonacci numbers and uses a function to determine
whether a number is a prime number.  Then a list is created to store the first 11 prime Fibonacci numbers
"""
from math import sqrt
import threading
import time

thread_lock = threading.Lock()

#### Create a generator that outputs Fibonacci numbers
def fibonacci_generator():
    """
    This generator yields numbers from the Fibonacci sequence
    :return: next number in the Fibonacci sequence
    """
    num_a = 0
    num_b = 1
    while True:
        yield num_a
        old_a = num_a
        num_a = num_b
        num_b = old_a + num_b

#### Create a function that determines whether a number is prime
def is_prime(num, prime_list):
    """
    This function determines if a number is a prime number and appends it to the list of numbers, else returns False
    :param num: number to be determined if it is prime
    :param prime_list: list of prime Fibonacci numbers
    :return: False is number is not prime
    """
    #time.sleep(.005)
    with thread_lock:
        #print("Number of Threads running: " + str(threading.active_count()))
        if (num <= 1):
            return False
        if (num == 2):
            prime_list.append(num)
        if (num % 2 == 0):
            return False

        i = 3
        while i <= sqrt(num):
            if num % i == 0:
                return False
            i = i + 2

        prime_list.append(num)

if __name__ == '__main__':
    #### Create a list to store the first 4 Fibonacci numbers that are also prime
    start = time.time()
    prime_fib_nums_list = []
    prime_threads = []
    fib_generator = fibonacci_generator()
    while len(prime_fib_nums_list) < 4:
        cur_num = next(fib_generator)
        prime_thread = threading.Thread(target=is_prime, args=(cur_num, prime_fib_nums_list))
        prime_thread.start()
        prime_threads.append(prime_thread)
    # for thread in prime_threads:
    #     thread.join()


    #### Do this again (appending 4 more fib primes to your list) so you end up with 8 Fibonacci primes)
    while len(prime_fib_nums_list) < 8:
        cur_num = next(fib_generator)
        prime_thread = threading.Thread(target=is_prime, args=(cur_num, prime_fib_nums_list))
        prime_thread.start()
        prime_threads.append(prime_thread)
    # for thread in prime_threads:
    #     thread.join()

    #### Do it one last time but only get three fib primes the final time (This may be a bit slower since numbers are so big)
    while len(prime_fib_nums_list) < 11:
        cur_num = next(fib_generator)
        prime_thread = threading.Thread(target=is_prime, args=(cur_num, prime_fib_nums_list))
        prime_thread.start()
        prime_threads.append(prime_thread)

    for thread in prime_threads:
        thread.join()
    end = time.time()
    #### Print the list to the console
    print("The first 11 prime numbers in the Fibonacci sequence are:\n" + str(prime_fib_nums_list))
    print(end - start)