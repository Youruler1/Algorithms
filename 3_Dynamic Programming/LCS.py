def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # Create a DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in bottom-up fashion
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Reconstruct the LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_str.reverse()
    return ''.join(lcs_str), dp[m][n]

if __name__ == "__main__":
    X = input("Enter first string: ")
    Y = input("Enter second string: ")
    lcs_string, length = lcs(X, Y)
    print(f"Longest Common Subsequence: {lcs_string}")
    print(f"Length of LCS: {length}")


# driver function will define both strings X and Y to be compared

# def LCS(X, Y):
#     # will return the length of the LCS, and the LCS itself

#     m = len(X)
#     n = len(Y)

#     dp = [[0] * (n + 1) for _ in range(m+1)]

#     for i in range(m):
#         for j in range(n):
#             if X[i] == Y[j]:
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:
#                 dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

#     lcs_str = []

