# Author: Jacob Schlaerth
# Date: 06/28/2020
import random
import time


def time_decorator(func):
    """decorator function that returns the time needed for a passed sorting algorithm to complete"""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(run_time, end="")
        return run_time
    return wrapper


def randList(n):
    """
    fills an list of length n with random integers between 0 and 10000
    :param n: length of list
    :return: list
    """
    rand_list = []
    for i in range(0, n):
        rand_list.append(random.randint(0, 10000))
    return rand_list


@time_decorator
def insertionSort(num_list):
    """
    sort a list of numbers via insertion sorting algorithm
    :param num_list: num_list[0] = how many numbers to sort
    :return: None, num_list is mutable
    """
    for ind in range(1, len(num_list)):
        current = num_list[ind]
        j = ind - 1
        while j >= 0 and current > num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = current


for i in range(10, 201, 10):
    random_list = randList(i)
    print("array of length", i, "sorted in ", end="")
    insertionSort(random_list)
    print(" seconds via insertion sort.")