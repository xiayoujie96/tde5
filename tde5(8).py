'''
Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas
''' 
lista = list(map(int, input('insira 10 numeros').split()))
if len(lista) != 10:
    print('errado')
a = int(input('insira o numero e verei se ele está na lista'))

for index, value in enumerate(lista):
    if value == a:
        print(f'posição de {a} é {index}', end=' ')