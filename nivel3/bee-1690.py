def menor_subconjunto_inalcancavel(arr):
    menorValor = 1

    for num in sorted(arr):
        if num > menorValor:
            return menorValor
        menorValor += num

    return menorValor

teste = int(input())

for _ in range(teste):
    tam = int(input())
    arr = list(map(int, input().split()))

    resultado = menor_subconjunto_inalcancavel(arr)
    print(resultado)
