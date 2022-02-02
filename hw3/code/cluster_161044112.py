
def find_most_profitable_cluster_BF(region_profit_list: list):
    if len(region_profit_list) < 2:
        print('Region_list_profit must be 2 dimensional list. (First row = address, Second row = profit)')
        return None

    if len(region_profit_list[0]) != len(region_profit_list[1]):
        print('Length of two dimension of argument list must be equal!')
        return None

    if len(region_profit_list[0]) < 1:
        print('Argument list is empty')
        return None

    if len(region_profit_list[0]) == 1:
        return region_profit_list.copy()

    max_start = -1
    max_end = -1
    g_max = float('-inf')

    for i in range(len(region_profit_list[1])):
        for j in range(i+1, len(region_profit_list[1])):
            sum_sublist = sum_list(region_profit_list[1][i:j+1])
            if sum_sublist > g_max:
                g_max = sum_sublist
                max_start = i
                max_end = j+1

    return region_profit_list[0][max_start:max_end], region_profit_list[1][max_start:max_end]


def sum_list(lst: list):

    _sum = 0
    for i in lst:
        _sum = _sum + i

    return _sum


def demo_5_a():

    _region_profit_list: list = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        [3,  -5,  2,  11,  -8,   9,  -5]
    ]

    regions, profits = find_most_profitable_cluster_BF(_region_profit_list)
    print('Table:\n', _region_profit_list[0], '\n', _region_profit_list[1])
    print('The most profitable cluster:\n', regions, '\n', profits)
    print('------------------------------------------')

    _region_profit_list: list = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        [333, -5, 2, 11, -8, 9, 500]
    ]

    regions, profits = find_most_profitable_cluster_BF(_region_profit_list)
    print('Table:\n', _region_profit_list[0], '\n', _region_profit_list[1])
    print('The most profitable cluster:\n', regions, '\n', profits)
    print('------------------------------------------')

    _region_profit_list: list = [
        ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        [344, -5, 2, 11, -8, 9, -5]
    ]

    regions, profits = find_most_profitable_cluster_BF(_region_profit_list)
    print('Table:\n', _region_profit_list[0], '\n', _region_profit_list[1])
    print('The most profitable cluster:\n', regions, '\n', profits)
    print('------------------------------------------')


demo_5_a()

