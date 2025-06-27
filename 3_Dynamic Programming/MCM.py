## DYNAMIC PROGRAMMING CODE FOR MATRIX CHAIN MULTIPLICATION (MCM)

def minops(dims, i, j, m, s):
    kopt = -1
    if i == j:
        return 0
    if m[i][j] != -1:
        return m[i][j]
    
    m[i][j] = float('inf')  # Important fix
    for k in range(i, j):
        aux = (minops(dims, i, k, m, s) +
               minops(dims, k+1, j, m, s) +
               dims[i]*dims[k+1]*dims[j+1])
        if aux < m[i][j]:
            m[i][j] = aux
            kopt = k
    s[i][j] = kopt
    return m[i][j]

def matrix_chain_order(dims):
    expr_len = len(dims) - 1  # Number of matrices
    m = [[-1 for _ in range(expr_len)] for _ in range(expr_len)]
    s = [[-1 for _ in range(expr_len)] for _ in range(expr_len)]

    # Initialize diagonal to 0
    for i in range(expr_len):
        m[i][i] = 0

    min_cost = minops(dims, 0, expr_len - 1, m, s)
    return min_cost, s

if __name__ == "__main__":
    dims = [10, 20, 30, 40]
    min_cost, s = matrix_chain_order(dims)
    print("Minimum cost:", min_cost)
