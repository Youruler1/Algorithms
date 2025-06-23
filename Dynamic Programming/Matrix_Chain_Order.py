def minops(dims, i, j, m, s):
    # if i>j : 
    kopt = -1
    if(i == j):
        return 0
    if(m[i][j] != -1): 
        return m[i][j]
    for k in range(i, j):
        aux = minops(dims, i,k,m,s) + minops(dims, k+1,j,m,s) + dims[i]*dims[k+1]*dims[j+1]
        if (m[i][j] > aux):
            m[i][j] = aux
            kopt =  k
    s[i][j] = kopt
    return m[i][j]


def matrix_chain_order(dims:list[int], begin, end, m=None, s=None):
    ## let begin and end be zero-indexed indices of target matrix slice
    expr_len = len(dims) - 1
    m = [[-1 for _ in range(expr_len)] for _ in range(expr_len)]
    s = [[-1 for _ in range(expr_len)] for _ in range(expr_len)]

    min_cost = minops(dims, i, j, m, s)
    # associative_map = partitionMatrices()

    return min_cost #and associative_map

if __name__ == "__main__":
    dims = [10,20,30,40]
    i = 0
    j = len(dims)-1
    matrix_chain_order(dims, i, j)