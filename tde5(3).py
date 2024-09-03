#Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois
lista = list(map(int, input('insira 3 numeros separados por espaço: ').split()))
if lista[0] > lista[1] + lista[2]:
    print('primeiro maior que soma dos dois')
else: 
    print('nao e maior')