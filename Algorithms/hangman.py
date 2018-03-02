import palavras
palavra = palavras.devolve_palavra().lower()
letrasAdivinhadas = ["_ " for x in range(len(palavra))]

while True:
    
    if "".join(letrasAdivinhadas) == palavra:
        break
        
    palpite = input("Digite uma letra: ").lower()
    
    if palpite == "querosair":
        break
    
    elif len(palpite) == 1 and palpite in palavra:
        for charIndex in range(len(palavra)):
            if palavra[charIndex] == palpite:
                letrasAdivinhadas[charIndex] = palpite

    print("".join(letrasAdivinhadas))
    
print("FIM DE JOGO!")
