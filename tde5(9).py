'''
 Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores.
'''
vlido = set(list(map(int, input('10').split())))
vpares = []
vimpares = []
for i in vlido:
    if i != 0:
        if i % 2 == 0:
            vpares.append(i)
        else: 
            vimpares.append(i)
print(vlido, vpares, vimpares)
