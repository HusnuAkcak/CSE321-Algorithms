def pack(box_w, prices, weights):
    
    if len(prices) == 0:
        return 0

    box = []
    max_price = 0
    while len(prices)>0 and box_w > 0:
        max_ind= fetch_most_valuable_ind(prices, weights)
        if weights[max_ind] > box_w:
            box.append((prices[max_ind]/weights[max_ind])*box_w)
            box_w = 0
        else:
            box.append(prices[max_ind])
            box_w = box_w - weights[max_ind]

        prices.pop(max_ind)
        weights.pop(max_ind)

    for price in box:   
        max_price = max_price + price

    print(box)
    return max_price 
    

def fetch_most_valuable_ind(prices, weights):

    if len(prices) == 0 :
        return None

    max_val = float('-inf')
    max_ind = 0
    for i in range(len(prices)):
        if prices[i]/weights[i] > max_val:
            max_val = prices[i]/weights[i] 
            max_ind = i

    return max_ind


arr_p1 = [60, 100, 120]
arr_w1 = [10, 20, 30]
W1 = 50

print("----------------------------------")
print("prices:", arr_p1)
print("weights:", arr_w1)
print("Capacity:",W1)
print("max_price:", pack(W1, arr_p1, arr_w1))
print("----------------------------------")


arr_p2 = [10, 100, 90, 85]
arr_w2 = [10, 50, 30, 20]
W2 = 65

print("prices:", arr_p2)
print("weights:", arr_w2)
print("Capacity:",W2)
print("max_price:", pack(W2, arr_p2, arr_w2))
print("----------------------------------")

arr_p3 = [50, 200, 90, 60]
arr_w3 = [10, 40, 30, 20]
W3 = 90

print("prices:", arr_p3)
print("weights:", arr_w3)
print("Capacity:",W3)
print("max_price:", pack(W3, arr_p3, arr_w3))
print("----------------------------------")

