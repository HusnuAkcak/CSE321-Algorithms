def merge_sort_and_count(arr):

    if len(arr) == 1:
        return 0, arr
    else:
        mid = len(arr)//2
        r_a, a = merge_sort_and_count(arr[:mid])
        r_b, b = merge_sort_and_count(arr[mid:])
        r_m, m = merge_and_count(a, b)
        return r_m+r_a+r_b, m

def merge_and_count(arr1, arr2):
    
    reverse_order = 0
    i = 0
    j = 0 
    res = []
    while i < len(arr1) and j < len(arr2):

        if arr1[i] <= arr2[j] :
            res.append(arr1[i])
            i = i+1
        else :
            res.append(arr2[j])
            reverse_order = reverse_order+len(arr1)-i
            j = j+1

    while i < len(arr1):
        res.append(arr1[i])
        i = i+1

    while j < len(arr2):
        res.append(arr2[j])
        j = j+1

    return reverse_order, res


test_arrays = [
    [2, 4, 1, 3, 5], 
    [6, 3, 5 ,2, 7],
    [1, 20, 6, 4, 5],
    [1, 9, 6, 4, 5, 0],
    [30, 43, 21, 10, 33]
]


for i in range(len(test_arrays)):
    ro, srtd = merge_sort_and_count(test_arrays[i])
    print("arr: {0}, REVERSE ORDERED PAIRS:{1}, sorted_v: {2}".format(test_arrays[i], ro, srtd))