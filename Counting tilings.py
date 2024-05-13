def count_tile_ways(n, m):
    # Define the set of possible row patterns
    patterns = set(['u' * m])
    for i in range(1, m):
        patterns.add('u' * i + 't' + 'u' * (m - i - 1))
        patterns.add('u' * i + 'A' + 'u' * (m - i - 1))

    # Initialize the dp table
    dp = [0] * (1 << m)
    dp[0] = 1  # Base case: empty row

    # Iterate over each row
    for i in range(n):
        new_dp = dp[:]  # Create a copy of the previous row
        for row_pattern in patterns:
            row_code = 0
            for j in range(m):
                if row_pattern[j] == 't':
                    row_code |= (1 << j)
                elif row_pattern[j] == 'A':
                    row_code |= (1 << j)
                    row_code |= (1 << (j + 1))

            for prev_row_code in range(1 << m):
                if not (prev_row_code & row_code):
                    new_dp[prev_row_code | row_code] += dp[prev_row_code]

        dp = new_dp

    return dp[(1 << m) - 1]

# Example usage
n, m = 4, 7
ways = count_tile_ways(n, m)
print(f"Number of distinct ways to fill a {n}x{m} grid: {ways}")
