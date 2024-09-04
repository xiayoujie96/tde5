'''
Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores
positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares, depois,
os números impares. Mostre o vetor antes de depois da modificação
'''
lista = sorted(list(map(int, input(': ').split())))
lista1 = []
lista2 = []
for i in lista:
        if i < 0:
           raise ValueError  
        if i % 2 == 0:
            lista1.append(i)
        else: 
            lista2.append(i)
print(lista1+lista2)
