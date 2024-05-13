def find_all_sums(weights):
    n = len(weights)
    max_sum = sum(weights)
    dp = [[False] * (max_sum + 1) for _ in range(n + 1)]

    # Base case: Sum 0 can always be formed by not taking any weight
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, max_sum + 1):
            if j >= weights[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - weights[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Collect all possible sums
    all_sums = []
    for j in range(max_sum + 1):
        if dp[n][j]:
            all_sums.append(j)

    return all_sums

# Example usage
weights = [3, 4, 5, 2]
all_sums = find_all_sums(weights)
print(f"All possible sums using weights {weights}: {all_sums}")
