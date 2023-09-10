"""
To add a sorting algorithm, implement it below by respecting algo_name(screen, array) prototype.
Then, add the complexity in the complexity dictionary in view.py ("algo_name": "complexity")
"""

import view

def bubble_sort(screen, array):
    for i in range(len(array) - 1):
        for j in range(1, len(array) - i):
            colored = [j-1, j]
            view.print_step(screen, array, colored)
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

def insertion_sort(screen, array):
    for i in range(1, len(array)):
        value = array[i]
        j = i-1
        while j >= 0 and value < array[j]:
            colored = [i, j]
            view.print_step(screen, array, colored)
            array[j+1] = array[j]
            j -= 1
        array[j+1] = value
        colored = [j+1]
        view.print_step(screen, array, colored)
    return array

def selection_sort(screen, array):
    for i in range(len(array)):
        min = array[i]
        idx = i
        for j in range(i+1, len(array)):
            colored = [idx, j]
            if array[j] < min:
                min = array[j]
                idx = j
            view.print_step(screen, array, colored)
        array[idx] = array[i]
        array[i] = min
        view.print_step(screen, array, colored)
    return array

def merge_sort(screen, array):
    def rec(arr):
        if len(arr) <= 1:
            return arr
        else:
            return merge(rec(arr[:(len(arr) // 2)]), rec(arr[(len(arr) // 2):]))
    def merge(arr1, arr2):
        if len(arr1) == 0:
            return arr2
        if len(arr2) == 0:
            return arr1
        view.print_step(screen, arr1 + arr2, [0, len(arr1)])
        if arr1[0] < arr2[0]:
            return [arr1[0]] + merge(arr1[1:], arr2)
        else:
            return [arr2[0]] + merge(arr1, arr2[1:])
    return rec(array)