def exp_bf(a, n):
    if a <= 0:
        return 0
    elif n == 0:
        return 1

    res = 1
    for i in range(n):
        res = res*a

    return res 


def exp_dq(a, n):
    
    if a == 0:
        return 0

    if n == 0:
        return 1

    if n == 1: 
        return a

    return exp_dq(a, n//2) * exp_dq(a, n-(n//2))


tests = [
    [5, 3], [4, 2], [0, 5], [5, 0], [2, 2]
]

for arr in tests:
    print("BF: {0}^{1} = {2}".format(arr[0], arr[1], exp_bf(arr[0], arr[1]) ) )
    print("DQ: {0}^{1} = {2}".format(arr[0], arr[1], exp_dq(arr[0], arr[1]) ) )

