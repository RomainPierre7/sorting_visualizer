# sorting_visualizer

## To launch

```
python3 main.py
```

## Algorithms list

* Bubble sort (n²)
* Insertion sort (n²)
* Selection_sort (n²)
* Merge sort (n*log(n))
*  ... ```TODO```

## To make a PR

* To add a sorting algorithm, implement it in algorithms.py by respecting algo_name(screen, array) prototype.

* Use `view.print_step(screen, array, colored)` to color in red the important values to visualize. `colored` is an array which take the indexes of `array` to color.

* Then, add the complexity in the complexity dictionary in view.py like this : `"algo_name": "complexity"`.