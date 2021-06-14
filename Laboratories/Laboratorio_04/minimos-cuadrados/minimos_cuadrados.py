import pylab as pl
import numpy as np
from sklearn import datasets

X = [[-0.682925] ,[1.051265] ,[1.531292] ,[0.348402] ,[0.269089] ,[-1.106335]]
Y = [-50.218465, 80.329757, 99.707264, 23.366514, 4.670804, -87.946511]

# menor en X
def men(X):
  min = X[0][0]
  for i in range(len(X)):
    if min > X[i][0]:
      min = X[i][0]
  return min

# mayor en X
def may(X):
  may = X[0][0]
  for i in range(len(X)):
    if may < X[i][0]:
      may = X[i][0]
  return may

# x*y
def mult(x, y):
  return x*y

# x**2
def cuadrado(x):
  return x**2

# sumatoria de x
def sumX(X):
  sum = 0
  for i in range(len(X)):
    sum += X[i][0]
  return sum

# sumatoria de y
def sumY(Y):
  sum = 0
  for i in range(len(Y)):
    sum += Y[i]
  return sum

# sumatoria de x*y
def sumXY(X, Y):
  sum = 0
  for i in range(len(X)):
    sum += mult(X[i][0], Y[i])
  return sum

# sumatoria de x**2
def sumXX(X):
  sum = 0
  for i in range(len(X)):
    sum += cuadrado(X[i][0])
  return sum

# w1
def w1(X, Y):
  N = len(X)
  w1 = (N*(sumXY(X, Y)) - (sumX(X))*(sumY(Y))) / \
      (N*(sumXX(X)) - cuadrado(sumX(X)))
  return w1

# w0
def w0(X, Y):
  N = len(X)
  w0 = (sumY(Y) - w1(X, Y)*(sumX(X))) / N
  return w0

# minimos cuadrados
def f(x):
  y = []
  for i in range(x.size):
    y.append(w1(X, Y)*x[i] + w0(X, Y))
  return y


if __name__ == "__main__":
  ans = "Sharon Rossely Alisson Chullunquía Rosas\n"
  ans += "Mínimos Cuadrados\n\n"
  ans += "Datos utilizados:\n"
  # imprimir datos
  for j in range(len(X)):
      ans += str(round(X[j][0], 6)) + "\t" + str(round(Y[j], 6)) + "\n"
  ans += '\n'
  ans += "Suma de valores de x: " + str(round(sumX(X), 6)) + '\n'
  ans += "Suma de valores de y: " + str(round(sumY(Y), 6)) + '\n'
  ans += "Suma de valores de x*y: " + str(round(sumXY(X, Y), 6)) + '\n'
  ans += "Suma de valores de x2: " + str(round(sumXX(X), 6)) + '\n'
  ans += '\n'

  ans += "Pendiente: " + str(round(w1(X, Y), 6)) + '\n'
  ans += "Intercepto: " + str(round(w0(X, Y), 6)) + '\n'

  with open('minimos-cuadrados.txt', 'w') as fileName:
      fileName.write(ans)

  pl.scatter(X, Y)
  x_real = np.arange(men(X)-0.5, may(X)+0.5, 0.1)
  y_real = []
  y_real = f(x_real)
  pl.plot(x_real, y_real, color='red')
  pl.show()
