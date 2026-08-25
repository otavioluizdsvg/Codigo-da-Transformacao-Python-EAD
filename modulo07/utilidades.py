'''
Potenciação

divisão

Multiplicação

Soma

Subtração
'''

def soma(a, b):

   return a + b


def subtração(a, b):

   return a - b


def multiplicação(a,b):

   return a * b


def dividir(a,b):

    if b == 0:
       return "Erro: Divisão por Zero não Permitida"
    return a / b

def divisão_inteira(a, b):
    '''
    Retorna apenas a parte inteira da divisão de 'a' por 'b'.
    Parâmetros: a (int/float), b (int/float)
    Retorno: o quociente inteiro ou uma mesagem de erro se  b == 0.
    '''
    if b == 0:
        return "Erro: Divisão por zero não é permitida"


def resto_divisao(a, b):
    '''
    Retorna apenas a parte inteira da divisão de 'a' por 'b'.
    Parâmetros: a (int/float), b (int/float)
    Retorno: o quociente inteiro ou uma mensagem de erro se b == 0
    '''





def calcular_madia(lista_numeros):

    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def e_par(numero):
    return numero % 2 == 0


def potencia(base, expoente):
    '''
    Eleva a base ao expoente (potenciação)
    Parâmetros: base (int/float), expoente (int/float)
    Return: o resultado de base elevado ao expoente.
    ''' 
    return base ** expoente





