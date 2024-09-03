#Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores 
# b) O produto deles 
# c) O quociente entre eles

lista = list(map(int, input('insira dois numeros').split()))
a = lista[0] + lista[1]
print(f'a soma dos dois é: {a}')
b = lista[0]*lista[1]
print(f'o produto é: {b}')
if lista[1] != 0:
    c = lista[0] / lista[1]
    print(f'o quociente é: {c}')
