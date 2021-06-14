import pylab as pl
import numpy as np
from sklearn import datasets

X = [[-0.682925] ,[1.051265] ,[1.531292] ,[0.348402] ,[0.269089] ,[-1.106335]]
Y = [-50.218465, 80.329757, 99.707264, 23.366514, 4.670804, -87.946511]

tasa = 0.001
pendiente = 1.0
intercepto = 0.0
iteraciones = 1000
w = [intercepto, pendiente]

# menor en X
def men(X):
  min = X[0][0]
  for i in range (len(X)):
    if min > X[i][0]:
      min = X[i][0]
  return min

# mayor en X
def may(X):
  may = X[0][0]
  for i in range (len(X)):
    if may < X[i][0]:
      may = X[i][0]
  return may

def DSRIntercepto(X,Y):
  sum = 0
  for i in range (len(X)):
    sum -= 2*(Y[i]-(w[0] + w[1] * X[i][0]))
  return sum

def DSRPendiente(X,Y):
  sum = 0
  for i in range (len(X)):
    sum -= 2*(Y[i]-(w[0] + w[1] * X[i][0]))*(X[i][0])
  return sum

# loss
def loss(j):
  if j == 0: # w0
    return DSRIntercepto(X,Y)
  elif j == 1: # w1
    return DSRPendiente(X,Y)

# gradiente
def f(x):
  y = []
  for i in range(x.size):
    y.append(w[1]*x[i] + w[0])
  return y

if __name__ == "__main__":
  ans = "Sharon Rossely Alisson Chullunquía Rosas\n"
  ans += "Gradiente Descendiente\n\n"
  ans += "Datos utilizados:\n"
  # imprimir datos
  for j in range(len(X)):
      ans += str(round(X[j][0], 6)) + "\t" + str(round(Y[j], 6)) + "\n"
  count = 0

  for i in range(iteraciones):
    w0_ant = w[0]
    w1_ant = w[1]
    for j in range(len(w)):
      w[j] = w[j] - tasa * loss(j)
      
    count += 1
    ans += '\n'
    ans += "Iteracion " + str(count) + '\n'
    ans += "Pendiente anterior = " + str(round(w1_ant,6)) + '\n'
    ans += "Intercepto anterior = " + str(round(w0_ant,6)) + '\n'
    ans += "Tasa de aprendizaje = " + str(tasa) + '\n'
    ans += "Derivada intercepto = "+ str(round(DSRIntercepto(X,Y),6)) + '\n'
    ans += "Derivada pendiente = "+ str(round(DSRPendiente(X,Y),6)) + '\n'
    ans += "Pendiente nueva = " + str(round(w[1],4)) + '\n'
    ans += "Intercepto nuevo = " + str(round(w[0],4)) + '\n'
    ans += '\n'

  with open('gradiente-descendiente.txt', 'w') as fileName:
    fileName.write(ans)

  pl.scatter(X,Y)
  x_real = np.arange(men(X)-0.5, may(X)+0.5,0.1)
  y_real = []
  y_real = f(x_real)
  pl.plot(x_real, y_real, color='red')
  pl.show()
