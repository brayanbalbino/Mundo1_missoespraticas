nint = int(input())

for teste in range(nint):
    ntest = int(input())
    cont = 0
    
    for div in range(1,ntest+1):
        if ntest % div == 0:
            cont = cont + 1
    if cont == 2:
        print(ntest,"eh primo")
    else:
        print(ntest,"nao eh primo")
