def coin_change(coins, n):
    # Create a table to store the minimum number of coins needed for each value
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 cents

    # Iterate over each value from 1 to n
    for value in range(1, n + 1):
        # Try every coin smaller than or equal to the current value
        for coin in coins:
            if coin <= value:
                # Update the minimum number of coins needed for the current value
                dp[value] = min(dp[value], dp[value - coin] + 1)

    # If it's impossible to make the target sum, return -1
    return dp[n] if dp[n] != float('inf') else -1

# Example usage
coins = [1, 5, 10, 25]
target_sum = 16
min_coins = coin_change(coins, target_sum)
print(f"Minimum number of coins needed to make {target_sum} cents: {min_coins}")
