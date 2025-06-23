import types


# brute force
def fibonacci(n: int) -> int :
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Top-down dynamic programming (memoization)
def fibonacci_top_down(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

# Bottom-up dynamic programming (tabulation)
def fibonacci_bottom_up(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    num = int(input("Enter the number to take fibonacci of: "))
    print(f"\nFibonacci of {num} is: {fibonacci(num)}")





