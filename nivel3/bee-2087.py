while True:
    n = int(input())
    if n == 0:
        break
    cnjt = []
    prfx = 0

    for _ in range(n):
        cnjt.append(input())

    for i in range(len(cnjt)):
        for j in range(i + 1, len(cnjt)):
            if cnjt[i].startswith(cnjt[j]) or cnjt[j].startswith(cnjt[i]):
                prfx = 1
                break
        if prfx:
            break

    if prfx:
        print('Conjunto Ruim')
    else:
        print('Conjunto Bom')
