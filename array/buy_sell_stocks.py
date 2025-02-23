prices = [7,1,5,3,6,4]

max_profit = 0
min_value = prices[0]

for index, j in enumerate(prices[1:]):
    # if j is 0:
    #     continue
    print(max_profit, j, min_value , '---at', index)
    max_profit = j - min_value if max_profit  <  j - min_value else max_profit

    if j < min_value:
        j = min_value

    print(max_profit)
print(max_profit)
