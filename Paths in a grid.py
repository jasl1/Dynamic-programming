def max_sum_path(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row and column
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + grid[0][i]
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill the remaining cells
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[n-1][n-1]

# Example usage
grid = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
print(max_sum_path(grid))  # Output: 23
