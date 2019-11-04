import random

w = 10
h = 10

# def get_sum(l, i, x):
#   sum = 0
#   for j in range(i+1):
#     sum += l[j]*x
#   return sum

# def calculation(l, b):
#   x = []
#   x.append(b[0] / l[0][0])
#   for i in range(1, h):
#     print("b : " + str(b[i]))
#     print("sum : " + str(get_sum(l[i], i, x[i-1])))
#     print("x : " + str(x[i - 1]))
#     print("l[] : " + str(l[i]))
#     print("l[i][i] : " + str(l[i][i]))
#     x.append((b[i] - get_sum(l[i], i, x[i-1])) / l[i][i])
#   print("x : " + str(x))
#   print()
#   return x

def get_sum(l, x):
  sum = float(0.0)
  for i in range(len(x)):
    sum += l[i] * x[i]
  return sum


def calculation(l, b):
  x = []
  x.append(b[0] / l[0][0])
  for i in range(1, len(b)):
    x.append((b[i] - get_sum(l[i], x)) / l[i][i])
  return x





# tworzę macierz L #
matrix = [[float(0.0) for x in range(w)] for y in range(h)]
for i in range(h):
  for j in range(w):
    if j <= i:
      matrix[i][j] = random.random()
###############################################################

# tworze macierz jednostkowa
identity_matrix = [[float(0.0) for x in range(w)] for y in range(h)]
for i in range(h):
  for j in range(w):
    if j == i:
      identity_matrix[i][j] = float(1.0)
################################################################
print("Macierz wyjsciowa :")
for i in range(w):
  print(matrix[i])
print('\n' + '\n')

print("Macierz jednostkowa :")
for i in range(w):
  print(identity_matrix[i])
print('\n' + '\n')

################################################################
first_invertible_matrix = []

for i in range(w):
  a = []
  for j in range(h):
    a.append(identity_matrix[j][i])
  first_invertible_matrix.append(calculation(matrix, a))

right_invertible_matrix = []

# wlasciwa macierz odwrotna #
for i in range(w):
  row = []
  for j in range(h):
    row.append(first_invertible_matrix[j][i])
  right_invertible_matrix.append(row)

print("Macierz odwrotna :")
for i in range(h):
  print(right_invertible_matrix[i])  

##############################################################

# obliczam iloczyn macierzy jednostkowej i odwrotnej LL-1#
product = []
print("\n"+"\n")
for i in range(h):
  a = []
  for j in range(w):
    s = 0
    for k in range(w):
      s += matrix[i][k] * right_invertible_matrix[k][j]
    a.append(s)
  product.append(a)


for i in range(len(product)):
  print(product[i])

error = 0.0
for i in range(len(product)):
  error += abs(1.0 - abs(product[i][i]))

print("\n" + "\n")
print("Error : " + str(error))
  
  