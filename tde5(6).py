#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
#Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é triangular.
def funcao():
    a = int(input('insira um numero: '))
    while True:
        for i in range(1, 50):
            c = i * (i+1) * (i+2)
            if c == a:
                print(f'o numero {a} é triangular, ele é fruto de {i} * {i+1} * {i+2}')
                break
    print(f'o numero {a} não é triangular')
    break
funcao()
        
