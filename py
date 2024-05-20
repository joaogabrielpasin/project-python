n = int(input('digite o lado 1'))

m = int(input('digite o lado 2'))

matriz = []

for i in range (n):
    matriz.append( '*' * m)
for i in range (n):
    print(matriz[i])

