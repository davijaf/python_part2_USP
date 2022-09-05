def conta_letras(frase, contar="vogais"):
    caracteres = 0
    if contar == "vogais":
        for i in range(len(frase)):
            if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
                caracteres += 1
    if contar == "consoantes":
        for i in range(len(frase)):
            if frase[i] != "a" and frase[i] != "e" and frase[i] != "i" and frase[i] != "o" and frase[i] != "u" and frase[i] != " ":
                caracteres += 1
    return caracteres
conta_letras('programamos em python')
# deve devolver 6
conta_letras('programamos em python', 'vogais')
# deve devolver 6
conta_letras('programamos em python', 'consoantes')
# deve devolver 13