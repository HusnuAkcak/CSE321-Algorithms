import random

def lamuto_partition(arr):
    
    pivot = arr[0]
    small = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            small = small + 1
            swap(arr, small, i)

    swap(arr, 0, small)
    return small


def swap(arr, a, b):
    
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def meaningful(arr, k):    

    s = lamuto_partition(arr)
    if s == k-1:
        return arr[s]
    elif s > k-1:
        return meaningful(arr[:s], k)
    else:
        return meaningful(arr[s+1:], k-s-1)


test_arrays = [
    [10  , 4   , 3    , 2    , 0  ], 
    [1   , 5.1 , 11   , 33   , 1  ],
    [0   , 1.1 , 1.2  , 20   , 3  ],
    [0   , 44  , 10.1 , 44.01, 8  ],
    [50.4, 34  , 2.2  , 0    , 50]
]


for arr in test_arrays:
    k = random.randint(1, len(arr))
    print("{0}th experiment is {1} in {2}".format(k, meaningful(arr, k), arr))