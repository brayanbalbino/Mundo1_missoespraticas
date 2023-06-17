while True:
    n = input()
    if n[0] == "-":
        break
    elif 'x' in n:
        ndec = int(n, 16)
        print(ndec)
    else:
        nhex = hex(int(n))
        print(nhex)
