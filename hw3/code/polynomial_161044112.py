
def calc_polynomial(poly, x):

    res = 0
    n = len(poly)
    for i in range(n):
        product = 1
        for j in range(0, i):
            product = x * product

        res = res + poly[n-i-1]*product

    return res


def calc_polynomial_demo():

    poly = [2, -6, 2, -1]
    x = 3
    res = calc_polynomial(poly, x)
    print('n:', len(poly), ' x:', x, 'polynomial:', poly)
    print('result:', res)
    print('----------------------------------')

    poly = [5, -4]
    x = 3
    res = calc_polynomial(poly, x)
    print('n:', len(poly), ' x:', x, 'polynomial:', poly)
    print('result:', res)
    print('----------------------------------')

    poly = [2, -1]
    x = 5
    res = calc_polynomial(poly, x)
    print('n:', len(poly), ' x:', x, 'polynomial:', poly)
    print('result:', res)
    print('----------------------------------')


calc_polynomial_demo()
