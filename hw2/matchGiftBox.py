# Ali is planning to visit his family. Before going, he bought n gifts of
# different sizes and n corresponding boxes. Write an efficient algorithm
# that helps Ali to match each gift to its corresponding box by
# getting help from the QuickSort algorithm. You are allowed to try
# a gift and box together, from which you can determine whether the gift
# is larger than the box, smaller than the box, or fits in the box exactly.
# However, there is no way to compare two gifts together or two boxes
# together.

def quicksort(gifts, boxes, lower, upper):
    if lower < upper:
        pivot = partition(gifts, boxes, lower, upper)
        quicksort(gifts, boxes, lower, pivot - 1)
        quicksort(gifts, boxes, pivot + 1, upper)
    else:
        return


def partition(gifts, boxes, lower, upper):
    pivot = gifts[upper]

    i = lower

    for j in range(lower, upper):
        if boxes[j] < pivot:
            swap(gifts, i, j)
            swap(boxes, i, j)
            i += 1

    swap(gifts, i, upper)

    return i


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


gifts = [50, 3, 5, 5, 8, 1, 2]
boxes = [4, 4, 6, 6, 10, 15, 56]
quicksort(gifts, boxes, 0, len(gifts) - 1)
for x in range(len(gifts)):
    print(gifts[x], " - ", boxes[x])
