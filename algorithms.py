import view

def bubble_sort(screen, array):
    return array

def insertion_sort(screen, array):
    return array

def selection_sort(screen, array):
    for i in range(len(array)):
        min = array[i]
        idx = i
        colored = [idx]
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
    return array