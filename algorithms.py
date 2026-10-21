import random


# bubble sort
# best case o(n) if the array is already sorted and swapped boolean optimization is present
# wors case and avg case o(n^2)
# definetion is having to pointers j and j+1 if in wrong order sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            return


# selection sort
# best case o(n^2)
# worst case and avg o(n^2)
# definition is just selecting the smallest element -----
# from the unsorted array (i>) and place it in i
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


# insertion sort
# best case o(n) if the array is already sorted
# worst and avg case o(n^2)
# definition is we start from second element to the first pointer------
# and compare it with the left array(sorted) if 1 swap didnt happen it means------
# element is in correct position
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    idx = left
    i, j = 0, 0
    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[idx] = L[i]
            i += 1
        else:
            arr[idx] = R[j]
            j += 1
        idx += 1
    while j < n2:
        arr[idx] = R[j]
        j += 1
        idx += 1

    while i < n1:
        arr[idx] = L[i]
        i += 1
        idx += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot_idx = random.randint(start, end)
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    pivot = arr[end]
    i = start - 1
    j = start
    while j < end:
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        j += 1
    arr[end] = arr[i + 1]
    arr[i + 1] = pivot
    quick_sort(arr, start, i)
    quick_sort(arr, i + 2, end)
