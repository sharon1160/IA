import numpy as np
import pylab as pl

def distanciaEuclidiana(centroide, punto):
    a = [float(centroide[1]), float(centroide[2])]
    b = [punto[1], punto[2]]
    return np.linalg.norm(np.array(a) - np.array(b))


def calcularDistancias(datos,centroides, colores):
    distancias = []
    for i in range (len(datos)):
        distC = []
        for j in range (len(centroides)):
            dist = distanciaEuclidiana(centroides[j],datos[i])
            distC.append(dist)
        distancias.append(distC)
    return distancias

def colorear(indice, menor, colores):
    # rojo
    if indice == 0:
        colores[1] = "red"
    # azul
    elif indice == 1:
        colores[1] = "blue"
    # amarillo
    elif indice == 2:
        colores[1] = "yellow"
    colores[2] = menor
    return colores

def minimo(distancias, colores):
    indice = 0
    for i in range (len(distancias)):
        menor = distancias[0][0]
        for j in range (len(distancias[0])):
            if distancias[i][j] < menor:
               menor = distancias[i][j]
               indice = j
        colores[i] = colorear(indice, menor, colores[i])
    return colores

def mostrar(matrix):
    cad = ""
    for i in range (len(matrix)):
        cad += "[ "
        for j in range (len(matrix[0])):
            cad += str(round(matrix[i][j],3)) + " "
        cad += "]\n"
    return cad

def mostrar2(matrix):
    cad = ""
    for i in range (len(matrix)):
        cad += "[ "
        for j in range (len(matrix[0])):
            cad += str(matrix[i][j]) + " "
        cad += "]\n"
    return cad

def suma(points):
    sumX = 0
    sumY = 0
    for i in range (len(points)):
        sumX += points[i][1]
        sumY += points[i][2]
    return [sumX, sumY]

def nuevoCentroide(colorIndex, datos,j):
    flag = ""
    points = []
    for i in range (len(colorIndex)):
        points.append(datos[colorIndex[i]-1])

    [sumX, sumY] = suma(points)
    if j == 0: flag = "C1"
    elif j == 1: flag = "C2"
    elif j == 2: flag = "C3"

    newCentroide = [flag, sumX/len(points), sumY/len(points)]
    return newCentroide

def actualizarCentroides(centroides, colores, datos):
    rojos = []
    azules = []
    amarillos = []
    for i in range (len(colores)):
        if colores[i][1] == "red":
            rojos.append(int(colores[i][0]))
        elif colores[i][1] == "blue":
            azules.append(int(colores[i][0]))
        elif colores[i][1] == "yellow":
            amarillos.append(int(colores[i][0]))
    colorIndex = [rojos, azules, amarillos]
    for j in range (len(centroides)):
        centroides[j] = nuevoCentroide(colorIndex[j], datos,j)
    return centroides

def graficar(datos, centroides):

    x_real = []
    y_real = []
    xc = []
    yc = []
    for i in range(len(datos)):
        y_real.append(datos[i][2])
        x_real.append(datos[i][1])

    for i in range(len(centroides)):
        y_real.append(centroides[i][2])
        x_real.append(centroides[i][1])
    
    colores=['black','black','black','black','black','black','black','black','black','black','black','black','black','black','black','red','blue','yellow']
    pl.scatter(x_real,y_real, color=colores)
    pl.show()

def plot(datos, centroides, colores):
    x_real = []
    y_real = []
    colors = []
    for i in range(len(datos)):
        y_real.append(datos[i][2])
        x_real.append(datos[i][1])
    for i in range(len(centroides)):
        y_real.append(centroides[i][2])
        x_real.append(centroides[i][1])
    
    for i in range (len(colores)):
        colors.append(colores[i][1])
    colors.append('red')
    colors.append('blue')
    colors.append('yellow')
    pl.scatter(x_real,y_real, color=colors)
    pl.show()


def main():
    cad = ""
    '''
    datos = np.array([[1, 6.57683632, -4.58428305], 
                    [2, 1.31490693, 6.89078593],
                    [3, 2.70173671, 8.48284937],
                    [4, 2.87468771, 7.2944393],
                    [5, 5.69739523, -4.85687328],
                    [6, -7.22634723, -2.09342083],
                    [7, 5.46199215, -4.48460727],
                    [8, 6.05444305, -5.86113356],
                    [9, 3.50889402, 6.77889201],
                    [10, -7.67310958, -2.83534704],
                    [11, 4.7099758, -5.25558146],
                    [12, -7.50294535, -3.76267107],
                    [13, -7.3107401, -2.50974733],
                    [14, -6.36151287, -2.10656881],
                    [15, 2.58398611, 6.63412394]])
    '''
    colores = np.array([[1, "", 0],
                        [2, "", 0],
                        [3, "", 0],
                        [4, "", 0],
                        [5, "", 0],
                        [6, "", 0],
                        [7, "", 0],
                        [8, "", 0],
                        [9, "", 0],
                        [10, "", 0],
                        [11, "", 0],
                        [12, "", 0],
                        [13, "", 0],
                        [14, "", 0],
                        [15, "", 0]])

    datos = np.array([[1, 8.67983498, 2.70124784], 
                [2, 8.44204393, 4.6202668],
                [3, -6.31298946, -3.57675469],
                [4, 8.17211728, 2.63388313],
                [5, 7.7525941, 3.90696234],
                [6, -5.27464973, -4.55386943],
                [7, -4.31870604, -4.41790017],
                [8, 6.40395937, 1.66981781],
                [9, 5.45405472, 1.17948257],
                [10, 5.74724736, 0.92345723],
                [11, 5.82396229, 2.18957944],
                [12, -5.85574745, -3.25898703],
                [13, -5.01140102, -3.93639035],
                [14, 6.06379634, 1.04611073],
                [15, 9.87461531, 3.87123505]])
    '''
    centroides = np.array([["C1", -7.50294535, -3.76267107],
                        ["C2", 2.70173671, 8.48284937],
                        ["C3", 6.05444305, -5.86113356]])
    '''
    centroides = np.array([["C1", -5.85574745, -3.25898703],
                        ["C2", 6.40395937, 1.66981781],
                        ["C3", 8.17211728, 2.63388313]])

    cad += "Algoritmo K-means\n"
    cad += '\n'
    cad += "Alumna: Sharon Chullunquía Rosas\n"
    cad += '\n'
    cad += "Puntos:\n"
    cad += '\n'
    cad += mostrar(datos)
    cad += '\n'
    graficar(datos, centroides)

    for i in range (3):
        cad += "-------------------------------------------------------------------\n"
        cad += '\n'
        cad += "ITERACION "+ str(i+1) + '\n'
        cad += '\n'
        cad += "Centroides Iniciales:\n"
        cad += '\n'
        cad += mostrar2(centroides)
        cad += '\n'
        # CALCULANDO DISTANCIAS
        distancias = calcularDistancias(datos,centroides, colores)
        cad += "Distancias:\n"
        cad += '\n'
        cad += mostrar(distancias)
        cad += '\n'
        # ENCONTRANDO EL MINIMO Y COLOREANDO
        colores = minimo(distancias, colores)
        cad += "Distancia Mínima y Color:\n"
        cad += '\n'
        cad += mostrar2(colores)
        cad += '\n'
        # ACTUALIZANDO CENTROIDES
        cad += "Centroides Nuevos:\n"
        cad += '\n'
        centroides = actualizarCentroides(centroides, colores, datos)
        cad += mostrar2(centroides)
        cad += '\n'
        plot(datos, centroides, colores)

        with open('k-means.txt', 'w') as f:
            f.write(cad)

if __name__ == "__main__":
    main()