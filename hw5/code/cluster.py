def cluster(lst):

    dl = len(lst)*[0]
    prev = 0
    for i in range(len(lst)):
        if lst[i]+prev > lst[i]:
            prev = dl[i] = lst[i]+prev
        else:
            prev = dl[i] = lst[i]
        
    return max(dl)


lst = [3, -5, 2, 11, -8, 9, -5]
print("max profit: {0}, arr: {1}".format(cluster(lst), lst))
print("=====================================================")
lst = [3, -5, 2, 11, -8, 9, -5, 100]
print("max profit: {0}, arr: {1}".format(cluster(lst), lst))
print("=====================================================")