import random
from colorama import Fore, init
from datetime import datetime

"""
Creaturas
"""

def creaturas_bd(tipo):
    pasivos = {
        'B': 'Burro',
        'N': 'Conejo',
        'G': 'Gallina',
        'C': 'Cerdo',
        'V': 'Vaca',
        'P': 'Panda',
        'L': 'Llama'
    }
    hostiles = {
        'A': 'Araña',
        'E': 'Enderman',
        'Z': 'Zombi',
        'B': 'Bruja',
        'O': 'Esqueleto',
        'W': 'Wither',
        'V': 'Vindicador'
    }
    if tipo == 'p':
        return pasivos
    if tipo == 'h':
        return hostiles


def generador_criaturas(hostil, pasiva):
    c_pasiva = list(creaturas_bd('p').keys())
    c_hostiles = list(creaturas_bd('h').keys())
    pasivos = []
    hostiles = []
    if hostil + pasiva > 50:
        return False
    else:
        cont = 0
        cont2 = 0
        while pasiva > 0:
            pasivos.insert(cont, random.choice(c_pasiva))
            cont += 1
            pasiva -= 1

        while hostil > 0:
            hostiles.insert(cont2, random.choice(c_hostiles))
            cont2 += 1
            hostil -= 1

        return [pasivos, hostiles]


def creatura_info(tipo, nombre, simbolo, fila, columna, fecha):
    creatura = {
        'Tipo': tipo,
        'Nombre': nombre,
        'Simbolo': simbolo,
        'Fila': fila,
        'Columna': columna,
        'Fecha': fecha
    }
    return creatura


def creaturas_activas(creaturas):
    creaturasDBP = creaturas_bd('p')  # Datos de creaturas pasivas
    creaturasDBH = creaturas_bd('h')  # Datos de creaturas hostiles
    pasivos = creaturas[0]
    hostiles = creaturas[1]
    creaturas = []

    for i in range(0, len(pasivos)):
        codigo = dict(filter(lambda x: x[0] == pasivos[i], creaturasDBP.items()))

        cre = creatura_info('Pasivo', tuple(codigo.values()), tuple(codigo.keys()), random.randint(0, 17),
                            random.randint(0, 17), datetime.now())
        creaturas.append(cre)
    for i in range(0, len(hostiles)):
        codigo = dict(filter(lambda x: x[0] == hostiles[i], creaturasDBH.items()))
        cre = creatura_info('Hostil', tuple(codigo.values()), tuple(codigo.keys()), random.randint(0, 17),
                            random.randint(0, 17), datetime.now())
        creaturas.append(cre)

    # print(creaturas)
    return tuple(creaturas)


def insertar_creaturas(matriz, creatura, simbolo, tipo):
    for i in range(0, 18):
        for j in range(0, 18):
            if creatura == (i, j):
                if tipo == 'Pasivo':
                    matriz[i][j] = Fore.BLUE + f'{simbolo}'
                else:
                    matriz[i][j] = Fore.RED + f'{simbolo}'


"""
Fin Creaturas
"""


def cordenadas_aleatorias():
    filas = [[random.choice([i for i in range(0, 10)]) for i in range(0, 4)] for i in range(0, 4)]
    return filas


def crear_mundo(creaturas_generadas):
    init()
    entidades = creaturas_activas(creaturas_generadas)
    cordenadas = []
    for i in entidades:
        print(f'{i["Tipo"]} {i["Nombre"][0]}  {i["Simbolo"][0]}  ({i["Fila"]},{i["Columna"]})')
        cordenadas.append(((i["Fila"], i["Columna"]), i["Simbolo"][0], i["Tipo"]))

    # print(cordenadas)
    filas = cordenadas_aleatorias()[0]
    columnas = cordenadas_aleatorias()[1]
    anchos = cordenadas_aleatorias()[2]
    largos = cordenadas_aleatorias()[3]
    # listas
    #
    # filas = [0, 3, 5, 6]
    # columnas = [1, 3, 11, 12]
    # anchos = [2, 9, 1, 4]
    # largos = [5, 2, 2, 1]

    # matriz
    matriz = []
    cont = 0
    for i in range(0, 18):
        matriz.append([0] * 18)
        for j in range(0, 18):

            if filas[0] <= i <= filas[0] + (largos[0] - 1) and columnas[0] <= j <= columnas[0] + (anchos[0] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[1] <= i <= filas[1] + (largos[1] - 1) and columnas[1] <= j <= columnas[1] + (anchos[1] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[2] <= i <= filas[2] + (largos[2] - 1) and columnas[2] <= j <= columnas[2] + (anchos[2] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            elif filas[3] <= i <= filas[3] + (largos[3] - 1) and columnas[3] <= j <= columnas[3] + (anchos[3] - 1):
                matriz[i][j] = Fore.GREEN + '#'
            else:
                matriz[i][j] = Fore.WHITE + '-'

    for i in range(0, len(cordenadas)):
        insertar_creaturas(matriz, cordenadas[i][0], cordenadas[i][1], cordenadas[i][2])

    for fila in matriz:
        for valor in fila:
            print(valor, end="  ")
        print()


if __name__ == '__main__':
    while True:
        creaturasp = int(input('Numero de creaturas pasivas: '))
        creaturash = int(input('Numero de creaturas Hostiles: '))
        if not generador_criaturas(creaturash, creaturasp):
            print('No se puede crear mas de 50 creaturas\n')
        else:
            crear_mundo(generador_criaturas(creaturash, creaturasp))
            break
