import pylab as pl
import numpy as np
from math import exp, log

# Función para hallar y estimado
def yEstimado(m, x, b):
  return 1 / (1+ exp(-(m * x + b)))

# Función Entropía Binaria Cruzada
def binaryCrossEntropy(m, X, b, Y):
  sum = 0
  for i in range(len(X)):
    sum += Y[i] * log(yEstimado(m, X[i], b)) + (1 - Y[i]) * log(1 - yEstimado(m, X[i], b))
  return sum * (-1)

# Función para hallar la derivada 
# en cuanto a la pendiente e intercepto
def gradient(y, x, m, b, opc):
  # slope
  if opc == 0:
    return (yEstimado(m, x, b) - y) * x
  # intercept
  elif opc == 1:
    return (yEstimado(m, x, b) - y)

# Función para probar los datos de prueba
def test(testX, testY, m, b, umbral):
  c = 0
  cad = "Test" +'\n'
  for i in range(len(testX)):
    if yEstimado(m, testX[i], b) >= umbral and testY[i] == 1:
      cad += "Primer dato "+str(testX[i])+" = "+str(yEstimado(m, testX[i], b))+", aprobado estimado = "+str(testY[i])+", Correcto" + '\n'
      c+=1
    elif yEstimado(m, testX[i], b) < umbral and testY[i] == 0:
      cad += "Primer dato "+ str(testX[i])+" = "+str(yEstimado(m, testX[i], b))+", aprobado estimado = " +str(testY[i])+", Correcto" + '\n'
      c+=1
    else:
      cad +="Primer dato "+str(testX[i])+" = "+str(yEstimado(m, testX[i], b))+", aprobado estimado = "+str(testY[i])+", Incorrecto" + '\n'
  cad += "Porcentaje de Acierto: "+ str((c * 100)/len(testX))+'%' + '\n'
  return cad

# Función para graficar
def plot(m, b, X, Y):
  pl.scatter(X,Y)
  x_real = np.arange(min(X)-1, max(X), 0.1)
  y_real = []
  for i in range(len(x_real)):
    y_real.append(yEstimado(m, x_real[i], b))
  pl.plot(x_real, y_real, color='yellowgreen')
  pl.show()

# Función para mostrar los arreglos
def show(a):
  cad = "x = {"
  for i in range(len(a)):
    cad += str(a[i]) 
    if i != len(a)-1: cad += ","
  cad += "}"
  return cad

# Función principal de regresión logistica
def logisticRegression(X, Y, testX, testY, trainX, trainY, m, b, iterations, tasa, umbral):
  cad = ""
  for i in range(iterations):
    dm = 0
    db = 0
    cad += "Iteración " + str(i+1) +'\n'
    cad += "Pendiente Anterior = " + str(round(m,6)) +'\n'
    cad += "Intercepto Anterior = " + str(round(b,6)) +'\n'
    error = binaryCrossEntropy(m, trainX, b, trainY)
    cad += "Error = " + str(round(error,6)) +'\n'
    cad += "Tasa de aprendizaje = "+ str(tasa) +'\n'
    for i in range(len(trainX)):
      dm += gradient(trainY[i], trainX[i], m, b, 0)
      db += gradient(trainY[i], trainX[i], m, b, 1)
    cad += "Derivada pendiente = " + str(round(dm,6)) +'\n'
    cad += "Derivada intercepto = " + str(round(db,6)) +'\n'
    m = m - tasa * dm
    b = b - tasa * db
    cad += "Pendiente nueva = " + str(round(m,4)) +'\n'
    cad += "Intercepto nuevo = " + str(round(b,4)) +'\n'
    cad += '\n'
  cad += test(testX, testY, m, b, umbral) +'\n'
  plot(m, b, X, Y)
  return cad

if __name__ == "__main__":
  X = [5, 7, 2, 13, 4, 15, 9, 4, 6, 1, 3, 10, 4, 10, 8, 20, 18, 15, 20, 12, 6, 12, 13, 14, 10, 6, 21, 25]
  Y = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
  umbral = 0.5
  trainX = [5, 7, 2, 13, 4, 15, 9, 4, 6, 1, 3, 10, 4, 10, 8, 20, 18, 15, 20, 12, 6, 12]
  trainY = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1]
  testX = [13, 14, 10, 6, 21, 25]
  testY = [1, 1, 1, 0, 1, 1]
  # pendiente
  m = -0.9874
  # intercepto
  b = -2.1789
  # tasa de aprendizaje
  tasa = 0.001
  # nro de iteraciones
  iterations = 100000
  cad = "Sharon Chullunquía Rosas" + '\n'
  cad += "Pendiente anterior = " + str(m) + '\n'
  cad += "Intercepto anterior = " + str(b) + '\n'
  cad += "Tasa de aprendizaje = " + str(tasa) + '\n'
  cad += "Cantidad de iteraciones = " + str(iterations) + '\n'
  cad += "Umbral = " + str(umbral) + '\n'
  cad += "Datos de Entrenamiento:" + '\n'
  cad += show(trainX) + '\n'
  cad += show(trainY) + '\n'
  cad += "Datos de Test:" + '\n'
  cad += show(testX) + '\n'
  cad += show(testY) + '\n'
  cad += '\n'

  cad += logisticRegression(X, Y, testX, testY, trainX, trainY, m, b, iterations, tasa, umbral)
  with open('regresion-logistica.txt', 'w') as fileName:
      fileName.write(cad)