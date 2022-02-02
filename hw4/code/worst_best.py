import math


def worst_best(arr):
    if len(arr) == 0:
        return None, None

    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        e_min = arr[0] if arr[0] < arr[1] else arr[1]
        e_max = arr[0] if arr[0] > arr[1] else arr[1]

        return e_min, e_max

    e_min1, e_max1 = worst_best(arr[0 : math.floor(len(arr)/2)])
    e_min2, e_max2 = worst_best(arr[math.ceil(len(arr)/2) : len(arr)])

    e_min = e_min1 if e_min1 < e_min2 else e_min2
    e_max = e_max1 if e_max1 > e_max2 else e_max2

    return e_min, e_max
    

test_arrays = [
    [],
    [10.5], 
    [-1, -5.1],
    [0, -1.1, -1.2],
    [0, 44, -10.1, 44.01],
    [50.4, 34, -2.2, 0, -50]
]

for arr in test_arrays:
    e_min, e_max = worst_best(arr)
    print("Min={0}, Max={1}, Arr={2}".format(e_min, e_max, arr))
