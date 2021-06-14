import math
import pandas as pd
import random
import numpy as np


def classify(datas, classes, numberClass, fruits):
  cantTrain = round(len(datas) * 0.8)
  cantTest = round(len(datas) * 0.2)

  datass = datas
  fruitss = fruits
  dataTest = []
  dataTrain = []
  fruitsTest = []
  fruitsTrain = []
  
  for i in range (cantTest):
    indice = random.randint(0, len(datass)-1)
    dataTest.append(datass[indice])
    fruitsTest.append(fruitss[indice])
    datass.remove(datass[indice])
    fruitss.remove(fruitss[indice])
  
  dataTrain = datass
  fruitsTrain = fruitss
  return [dataTest, dataTrain, fruitsTest, fruitsTrain]

def get_key(val, distancias):
    for key, value in distancias.items():
         if val == value: return key
    return "No existe tal clave"

def distanciaEuclidiana(point, pointTrain):
  return np.sqrt(np.sum(np.square(np.array(point) - np.array(pointTrain))))

def kMenores(distancias, n, k):
  arr = []
  for key in distancias:
    arr.append(distancias[key])
  arr.sort()
  menores = []
  for i in range(k):
    menores.append(arr[i])
  return menores

def knn(dataTrain, point, k, fruitsTrain, fruitsTest):
  distanciasSet = {} # es un diccionario
  for i in range(len(dataTrain)):
    distancia = distanciaEuclidiana(point, dataTrain[i]) # es un numero
    distanciasSet [str(dataTrain[i])] = [distancia,fruitsTrain[i]]

  vecinos = kMenores(distanciasSet, len(distanciasSet), k)
  return [vecinos, distanciasSet]

def mostrarVecinos(k_menores, distancias):
  cad = "Vecinos más cercanos y sus distancias: \n"
  for i in range(len(k_menores)):
    cad += str(get_key(k_menores[i],distancias)) +' -> '+ str(k_menores[i][0]) +" de clase "+ str(k_menores[i][1]) +"\n"
  return cad

def getK(dataTrain):
  k = round(math.sqrt(len(dataTrain)))
  if k % 2 == 0:
    k += 1
  return k

def contar_veces(elemento, lista):
  veces = 0
  for i in lista:
      if elemento == i:
          veces += 1
  return veces

def getClass(k_menores, classes):
  classest = []
  for i in range (len(classes)):
    classest.append(k_menores[i][1])

  veces = 0
  rpta = ""
  for i in range (len(classes)):
    vecesm = contar_veces(classest[i], classest)
    if veces < vecesm:
      veces =vecesm
      rpta = classest[i]
  return rpta

def obtenerData(archivo, nfila, ncol):
  lista = []
  for i in range (nfila):
    list = []
    for j in range (1,ncol):
      list.append(archivo.iloc[i,j])
    lista.append(list)
  return lista

def obtenerClase(archivo,col,icol):
  lista = []
  for i in range(len(archivo[col])):
    lista.append(archivo.iloc[i,icol])
  return lista

#### MAIN ####

cad = "Alumna: Sharon Chullunquía Rosas\n"

classes = ["apple", "mandarin", "orange", "lemon"]

archivo = pd.read_csv('fruit.csv')
tam = len(archivo["fruit_name"])

#original
datas = obtenerData(archivo,tam,5)
fruits = obtenerClase(archivo,"fruit_name",0)

#copy
datas_ = obtenerData(archivo,tam,5)
fruits_ = obtenerClase(archivo,"fruit_name",0)

[dataTest, dataTrain, fruitsTest, fruitsTrain] = classify(datas_, classes, len(classes), fruits_)

#k
k = getK(dataTrain)

cad += "\nAlgoritmo: Knn\n"

cad += "\nDatos de entrenamiento:\n\n" 
for i in range (len(dataTrain)):
  cad += str(fruitsTrain[i]) + " : " +str(dataTrain[i]) +"\n"
cad += "\nDatos de prueba:\n\n"
for i in range (len(dataTest)):
  cad += str(fruitsTest[i]) + " : " + str(dataTrain[i]) +"\n"
cad += "\n"

aciertos = 0
# calculando knn para cada punto de prueba
for i in range (len(dataTest)):
  cad += "\nDato de prueba: " + str(dataTest[i]) + "\n"
  cad += "Clase real: "+ str(fruitsTest[i]) +"\n"
  [k_menores, distancias] = knn(dataTrain,dataTest[i],k,fruitsTrain, fruitsTest)
  cad += mostrarVecinos(k_menores, distancias)
  cad += "Clase estimada: " + str(getClass(k_menores, classes)) + "\n"
  if fruitsTest[i] == getClass(k_menores, classes):
    aciertos +=1

acuracy = aciertos/len(dataTest)
cad += "\nTasa de acierto: " + str(acuracy) + " %\n"

with open('knn.txt', 'w') as f:
    f.write(cad)

