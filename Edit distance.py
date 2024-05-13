def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    
    # Create a 2D table to store the edit distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],  # Deletion
                                    dp[i][j - 1],  # Insertion
                                    dp[i - 1][j - 1])  # Substitution
    
    # The edit distance is stored in the bottom-right corner of the table
    return dp[m][n]

# Example usage
str1 = "SATURDAY"
str2 = "SUNDAYS"
edit_dist = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is {edit_dist}")
