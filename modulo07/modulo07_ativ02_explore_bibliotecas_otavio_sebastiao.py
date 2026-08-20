'''
Progamador: as variaveis, serão inseridas no app - BACK-End
'''
import utilidades
import datetime
from faker import FAKER


fake = FAKER('pt_BR')


print('***Dados Criados - Prova de Matemática***')
print(f'Nome de Mentira: {fake.name()}')
print(f'E-Mail de Mentira: {fake.email()}')
print(f'Telefone de Mentira: {fake.phone_number()}')


print(f'Dados da Prova de Mentira ***')
agora = datetime.datetime.now()
print(f'Sua prova foi concluida : {agora.strftime('%d/%m/%YYYY %H:%M')}')


num1 = 10
num2 = 5

print('⚙ 🎃Teste de utilidades ⚙ 🎃')
print('⚙ 🎃número utilizados:{num1} e {num2}')


print(f'Usando Adição ({num1} + {num2}) :', utilidades.soma(num1, num2))


print(f'Usando Subtração({num1} - {num2}) :', utilidades.subtrair(num1, num2))


print(f'Usando Multiplicação({num1} * {num2}) :', utilidades.multiplicar(num1, num2))


print(f'Usando Divisão({num1} / {num2}) :', utilidades.dividir(num1, num2))


print(f'Usando Divisão Inteira({num1} // {num2}) :', utilidades.divisao_inteira(num1, num2))


print(f'Usando Resto da Divisão({num1} % {num2}) :', utilidades.resto_dividir(num1, num2))


print(f'Usando Potenciação({num1} ^ {num2}) :', utilidades.potencia(num1, num2))

print("\n=== TESTE DE SEGURANÇA (DIISÃO POR ZERO) ===")
print("Divisão por zero:", utilidades.dividir(10, 0))
