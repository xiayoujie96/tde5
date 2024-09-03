#Ler 4 números inteiros e calcular a soma dos que forem par.
lista = list(map(int, input('insira aqui 4 numeros e somarei os pares: ').split()))
a = 0
for i in lista:
    if i % 2 == 0:
        a += i
print(a)