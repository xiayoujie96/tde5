#Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100
def funcao():
    numero = int(input('insira o seu numero e darei uma tabela dele multiplicado de 1 até 10: '))
    a = 1
    while a != 11:
        b = numero*a
        a += 1
        print(b, end=' ')
funcao()
print('\n')
def funcao2():
    tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numero = int(input('Insira o seu número e darei uma tabela dele multiplicado de 1 até 10: '))
    for i in tabela:
        print(numero*i, end=' ')
funcao2()