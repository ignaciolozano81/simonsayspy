import random
lista = []
partida = bool
partida = True

while partida == True:
    recorrida = 0
    numero = random.randint(1, 4)
    lista.append(numero)
    print(lista)
    for i in lista:
        valor = int(input())
        if valor == lista[recorrida]:
            recorrida = recorrida + 1
        else:
            print("perdiste!!")
            sn = input("¿nueva partida? S/N: " )
            if sn == ('s' or 'S'):
                partida = True
                lista = []
                break
            elif sn == ('n' or 'N'):
                partida = False

## VA QUEDANDO FALTA VER ENTER AUTOMÁTICO
## Y LAS PAUSAS Y BOORAR PANTALLA
