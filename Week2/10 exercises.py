# 1. Question 1 Assinale as alternativas CORRETAS:

# Módulo podem se tornar uma entrada para o interpretador Python e assim ele é chamado de script
# Módulos servem para organizar melhor nosso código
# Módulos são compostos por funções (definições) e podem ter outros comandos (statements)
# Módulos é o mesmo que funções

# 2. Question 2 Considere o seguinte código armazenado dentro do arquivo trataString.py:

def fazAlgo(string):
    pos = len(string)-1
    stringMi = string.lower()
    string = string.upper()
    stringRe = ""
    while pos >= 0:
        if string[pos] == 'A' or string[pos] == 'E' or string[pos] == 'I' or string[pos] == 'O' or string[pos] == 'U':
            stringRe = stringRe + string[pos]
        else:
            stringRe = stringRe + stringMi[pos]
        pos = pos - 1
    return stringRe

if __name__ == "__main__":
    print(fazAlgo("teste"))
    print(fazAlgo("o ovo do avestruz"))
    print(fazAlgo("A CASA MUITO ENGRAÇADA"))
    print(fazAlgo("A TELEvisão queBROU"))
    print(fazAlgo("A Vaca Amarela"))
