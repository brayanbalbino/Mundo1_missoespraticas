while True:
    try:
        primeiro = input().lower()
        segundo = input()
        texto = input()
        palavras = texto.replace('<', '.<').replace('>', '>.').split('.')
        substituição = ""
        fraseNova = ""

        for palavra in palavras:
            novaPalavra = palavra
            if novaPalavra != '':
                if novaPalavra[0] == '<':
                    substituição += novaPalavra.lower().replace(primeiro, segundo)
                else:
                    substituição += novaPalavra

        palavras2 = texto.split(' ')
        palavras3 = substituição.split(' ')
        
        for nIndex in range(len(palavras3)):
            if palavras2[nIndex].lower() == palavras3[nIndex]:
                fraseNova += palavras2[nIndex] + ' '
            else:
                fraseNova += palavras3[nIndex] + ' '
        
        print(fraseNova[0:len(fraseNova) - 1])
    except EOFError:
        break
