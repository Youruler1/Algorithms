#include <iostream>
#include <vector>

// Function to compute nth Fibonacci number using memoization
int fibonacci(int n, std::vector<int>& memo) {
    if (n <= 1)
        return n;
    if (memo[n] != -1)
        return memo[n];
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

int main() {
    int n;
    std::cout << "Enter n: ";
    std::cin >> n;

    std::vector<int> memo(n + 1, -1);
    std::cout << "Fibonacci(" << n << ") = " << fibonacci(n, memo) << std::endl;

    return 0;
}