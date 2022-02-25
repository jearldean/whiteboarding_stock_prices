#!/usr/bin/python

def best(stock_prices):
    """"Given a list of prices, return the maximum profit.
    If no profit is possible, return 0.
      >>> best([15, 10, 20, 22, 1, 9])
      12
      >>> best([1, 2, 3, 4, 5])
      4
      >>> best([2, 3, 10, 6, 4, 8, 1])
      8
      >>> best([7, 9, 5, 6, 3, 2])
      2
      >>> best([0, 100])
      100
      >>> best([5,4 ,3, 2, 1])
      0
      >>> best([100])
      0
      >>> best([100, 0])
      0
      >>> best([])
      0
    """

    """#  INITIAL SOLUTION
    
    if len(stock_prices) == 0:
        return 0

    # Can be done in 1 for and 2 ifs...
    best_price_to_sell = max(stock_prices)

    for indx, item in enumerate(stock_prices):
        # print(indx, item)
        if item == best_price_to_sell:
            best_price_to_sell_indx = indx  # 1

    if best_price_to_sell_indx == 0:
        return 0

    if len(stock_prices[:best_price_to_sell_indx]) > 0:
        best_price_to_buy = min(stock_prices[:best_price_to_sell_indx])
        max_profit = (best_price_to_sell - best_price_to_buy)
        if max_profit > 0:
            return max_profit
        else:
            return 0
    else:
        return 0

    """

    # CHALLENGE: Do it in 1 for and 2 ifs...

    # Hmmm, how about 3 if's and zero for-loops?
    if stock_prices:
        best_price_to_sell = max(stock_prices)
        best_price_to_sell_indx = stock_prices.index(best_price_to_sell)  # Had to look this up
        range_to_find_best_price_to_buy = stock_prices[:best_price_to_sell_indx]
        if range_to_find_best_price_to_buy:
            best_price_to_buy = min(range_to_find_best_price_to_buy)
            if best_price_to_sell > best_price_to_buy:
                return best_price_to_sell - best_price_to_buy
            else:
                return 0
        else:
            return 0
    else:
        return 0



if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GREAT JOB!")
    print()