# Author: Jacob Schlaerth
# Date: 06/28/2020
import random
import time


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


def mergeSort(num_list):
    """
    sorts a list via merge sorting algorithm
    :param num_list: num_list[0] = number of elements to be sorted
    :return: none, num_list is mutable
    """
    if len(num_list) > 1:
        middle = len(num_list) // 2  # integer divide to find middle
        left = num_list[:middle]  # slice list into right and left halves
        right = num_list[middle:]

        mergeSort(left)  # recursive call
        mergeSort(right)  # recursive call

        i = 0  # init variables
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1


for i in range(10, 201, 10):
    random_list = randList(i)
    print("array of length", i, "sorted in ", end="")
    start_time = time.perf_counter()
    mergeSort(random_list)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print(run_time, end="")
    print(" seconds via merge sort.")