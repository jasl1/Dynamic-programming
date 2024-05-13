def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with 1 for all elements

    # Compute the length of the longest increasing subsequence ending at each index
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in dp, which represents the length of the longest increasing subsequence
    return max(dp)

# Example usage
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"Length of the longest increasing subsequence: {longest_increasing_subsequence(arr)}")
