
import numpy
import matplotlib.pyplot as mpl

db = open('aerogerador.dat', 'r')
ldb = db.readlines()
db.close()

k = int(input("Grau do polinômio :"))
n = len(ldb)
dataV = numpy.zeros(len(ldb)).reshape(len(ldb), 1)
dataP = numpy.zeros(len(ldb)).reshape(len(ldb), 1)
data = numpy.zeros(len(ldb)*2).reshape(len(ldb), 2)
X = numpy.ones(len(ldb)*(k + 1)).reshape(len(ldb), (k + 1))

sma_y = 0
i = 0
while i < len(ldb):
    dataV[i] = float(ldb[i].split()[0])
    dataP[i] = float(ldb[i].split()[1])
    data[i, 0] = dataV[i]
    data[i, 1] = dataP[i]
    j = 0
    while j < (k + 1):
        X[i][j] = (dataV[i]) ** j
        j = j + 1
    i = i + 1
Xt = X.transpose()
XtX = numpy.dot(Xt, X)
XtY = numpy.dot(Xt, dataP)
XtXi = numpy.linalg.inv(XtX)
B = numpy.dot(XtXi, XtY)
Y = numpy.dot(X, B)
my = float(dataP.mean())
SQe = 0
Syy = 0
i = 0
while i < n:
    SQe = SQe + (dataP[i] - Y[i]) ** 2
    Syy = Syy + (dataP[i] - my) ** 2
    i = i + 1
R2 = 1 - (SQe / Syy)
R2aj = 1 - ((SQe / (n-k+1)) / (Syy / (n - 1)))
print("R2 = "+str(R2))
print("R2aj = "+str(R2aj))

mpl.plot(dataV, dataP, '.', label='Dados')
mpl.plot(dataV, Y, '-', label='Regresão')
mpl.title('Aerogerador   { ' + " R2 = "+str(R2) + ", R2aj = "+str(R2aj)+" }")
mpl.ylabel('Potência Gerada')
mpl.xlabel('Velocidade')
mpl.grid()
mpl.legend()
mpl.show()
