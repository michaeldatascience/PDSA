def coinChange(coins, amount):
    maxamt = amount +1
    dp = [maxamt] * (maxamt)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, maxamt):
            dp[x] = min (dp[x], dp[x-coin] +1)

    if dp[amount]==maxamt:
        return -1
    else:
        return dp[amount]


def __coinChange(coins, amount):
    # Initialize dp array with values greater than amount
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # base case

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1



def _coinChange(coins, amount):
    # Initialize dp array with values greater than amount
    MAX = amount + 1  # define a constant for maximum value
    dp = [MAX] * (amount + 1)
    
    # Base case: amount = 0
    dp[0] = 0

    # Iterate over each coin type
    for coin in coins:
        print(f'using coin: {coin} till {amount+1}')
        # For each coin, start from its value and go up to the desired amount
        for x in range(coin, amount + 1):
            print (f'x: {x} coin{coin}')
            # Without the current coin, how many coins would have been needed for x amount?
            without_this_coin = dp[x]
            print(f'without this coin {without_this_coin}')

            # With the current coin, how many coins would be needed for x amount?
            with_this_coin = dp[x - coin] + 1
            print(f'with this coin {with_this_coin}')

            # Now, choose the minimum of the two
            if without_this_coin < with_this_coin:
                dp[x] = without_this_coin
                print(f'without_this_coin {without_this_coin} chosen')
            else:
                print(f'with_this_coin {with_this_coin} chosen')
                dp[x] = with_this_coin

    # If we haven't found a solution, return -1, otherwise return the solution
    if dp[amount] == MAX:
        return -1
    else:
        return dp[amount]


coins = [2,3,5]
sum = 11

changeneeded = coinChange(coins,sum)
print(f'for sum of {sum} change needed {changeneeded}')