class Carro:
    pass

meu_carro = Carro()

meu_carro.ano = 1968
meu_carro.modelo = "fusca"
meu_carro.cor = "azul"

carro_do_ime = Carro()
carro_do_ime.ano = 1981
carro_do_ime.modelo = "Brasília"
carro_do_ime.cor = "amarelo"

novo_fusca = meu_carro
novo_fusca.ano += 10
print(meu_carro.ano)