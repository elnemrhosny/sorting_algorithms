#!/bin/python3
import random
import time

import matplotlib.pyplot as plt

from algorithms import (
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)


# generating array function
def generate_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(1, size))
    return arr


# small helper function to return micro seconds
def to_micro_seconds(time_taken):
    return time_taken * 1_000_000


# Ask user which sorting alrgorithms he wants to test
# 'bubble', 'selection', 'insertion', 'merge', 'quick', 'heap'; 'q' finishes selection
print(
    "Enter desired algos here('bubble' , 'selection' , 'insertion' , 'merge' , 'quick' , 'heap') then 'q' to quit or 'all' for all "
)
algos = {
    "bubble": ["bubble", False],
    "selection": ["selection", False],
    "insertion": ["insertion", False],
    "merge": ["merge", False],
    "quick": ["quick", False],
    "heap": ["heap", False],
}
while True:
    algo = input("Desired algorithm : ")
    if algo == "all":
        for key in algos.keys():
            algos[key][1] = True
        break
    elif algo == "q":
        break
    try:
        algos[algo][1] = True
    except KeyError:
        print(
            "The algo name you entered is incorrect choose from ('bubble' , 'selection' , 'insertion' , 'merge' , 'quick' , 'heap')"
        )


# Ask user if he wants to print input and output
# take input from user , user can put array sizes one by one then "q" when finished
# or can put "def" to work with the internally create random arrays
print_input = input("Enter 'y' if you want to print input arrays or 'n' if you dont : ")
print_output = input(
    "Enter 'y' if you want to print output arrays or 'n' if you dont : "
)
print(
    "You will be prompted to enter the sizes of arrays , Enter 'q' when finished or Enter 'def' to use default arrays"
)
sizes = []
while True:
    user_input = input("Enter the size of the array: ")
    if user_input == "q":
        break
    elif user_input == "def":
        sizes = [100, 1000, 5000, 10000, 25000]
        break
    try:
        size = int(user_input)
        sizes.append(int(user_input))
    except ValueError:
        print("That is not a valid number , try again (Enter 'q' when finished)")


results = {"bubble": [], "selection": [], "insertion": [], "merge": [], "quick": [], "heap": []}
n = len(sizes)

# comment out print statement if needed
for size in sizes:
    arr = generate_array(size)
    # print input if asked
    if print_input == "y":
        print("Input array : ", arr)
    if algos["bubble"][1] == True:
        arr1 = arr.copy()
        start = time.perf_counter()
        bubble_sort(arr1)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["bubble"].append(total_time)
        if print_output == "y":
            print(
                "Bubble sort sorted array : ",
                arr1,
                "Time taken(micro seconds) : ",
                total_time,
            )

    if algos["selection"][1] == True:
        arr2 = arr.copy()
        start = time.perf_counter()
        selection_sort(arr2)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["selection"].append(total_time)
        if print_output == "y":
            print(
                "Selection sort sorted array : ",
                arr2,
                "Time taken(micro seconds) : ",
                total_time,
            )

    if algos["insertion"][1] == True:
        arr3 = arr.copy()
        start = time.perf_counter()
        insertion_sort(arr3)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["insertion"].append(total_time)
        if print_output == "y":
            print(
                "Insertion sort sorted array : ",
                arr3,
                "Time taken(micro seconds) : ",
                total_time,
            )
    if algos["merge"][1] == True:
        arr4 = arr.copy()
        start = time.perf_counter()
        merge_sort(arr4, 0, len(arr4) - 1)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["merge"].append(total_time)
        if print_output == "y":
            print(
                "Merge sort sorted array : ",
                arr4,
                "Time taken(micro seconds) : ",
                total_time,
            )

    if algos["quick"][1] == True:
        arr5 = arr.copy()
        start = time.perf_counter()
        quick_sort(arr5, 0, len(arr5) - 1)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["quick"].append(total_time)
        if print_output == "y":
            print(
                "Quick sort sorted array : ",
                arr5,
                "Time taken(micro seconds) : ",
                total_time,
            )

    if algos["heap"][1] == True:
        arr6 = arr.copy()
        start = time.perf_counter()
        heap_sort(arr6)
        end = time.perf_counter()
        total_time = to_micro_seconds(end - start)
        results["heap"].append(total_time)
        if print_output == "y":
            print(
                "Heap sort sorted array : ",
                arr6,
                "Time taken(micro seconds) : ",
                total_time,
            )

    print("\n")


# we need to have more than 1 array for the graph to work
if len(results["bubble"]) != 0:
    plt.plot(sizes, results["bubble"], marker="o", label="Bubble Sort")
if len(results["selection"]) != 0:
    plt.plot(sizes, results["selection"], marker="o", label="Selection Sort")
if len(results["insertion"]) != 0:
    plt.plot(sizes, results["insertion"], marker="o", label="Insertion Sort")
if len(results["merge"]) != 0:
    plt.plot(sizes, results["merge"], marker="o", label="merge Sort")
if len(results["quick"]) != 0:
    plt.plot(sizes, results["quick"], marker="o", label="Quick Sort")
if len(results["heap"]) != 0:
    plt.plot(sizes, results["heap"], marker="o", label="Heap Sort")
plt.xlabel("Array Size")
plt.ylabel("Runtime (micro seconds)")
plt.title("Sorting Algorithm Runtime")
plt.legend()
plt.show()
