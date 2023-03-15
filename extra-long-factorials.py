def extraLongFactorials():
    n = int(input())
    
    for i in range(n, 1, -1):
        n = n*(i-1)

    return n     

print(extraLongFactorials())


