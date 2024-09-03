'''
A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. 
Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido
'''
lista = sorted(list(map(int, input('insira 10 numeros separados por espaço: ').split())))
if len(lista) != 10:
    print('não inseriu 10 numeros')
else: 
    print(f'O valor maximo é: {lista[9]}')
    print(f'A amplitude amostral é de: {lista[9] - lista[0]}')