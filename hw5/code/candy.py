def candy(price_list, length_list, candy_size):

    dl = (1+len(price_list))*[0]
    dl[0] = 0
    candy_index = length_list.index(candy_size)
    # for i in range(1, len(length_list)):
    max_profit = price_list[candy_index]
    for j in range(len(length_list)):
        part1 = candy_size - length_list[j];
        if part1<=0:
            continue
        
        p1_price = price_list[length_list.index(part1)]
        p2_price = price_list[j]
        
        dl[j] = p1_price + p2_price

    return max(max_profit, max(dl))



price_list = [1, 5, 8, 9, 10, 17, 17, 20]
length_list = [1, 2, 3, 4, 5, 6, 7, 8]
candy_size = 8
mp = candy(price_list, length_list, candy_size)
print("max profit is", mp)
