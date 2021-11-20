def tinhGT(n):
    if n <= 1:
        return 1
    return n*tinhGT(n-1)