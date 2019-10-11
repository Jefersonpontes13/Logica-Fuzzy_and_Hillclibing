# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import random

fig = plt.figure()
ax = fig.gca(projection='3d')

X = np.arange(0, 20, 1)
Y = np.arange(0, 20, 1)

X, Y = np.meshgrid(X, Y)
Z = abs(X * np.sin(Y * np.pi / 4) + Y * np.sin(X * np.pi / 4))

# plot superficie.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(0, 40)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

it = 0
at = np.zeros(3).reshape(1, 3)
pr = np.zeros(3).reshape(1, 3)
viz = np.zeros(16).reshape(8, 2)
res_viz = np.zeros(8).reshape(8, 1)


def f_pro(p):
    global arq
    global it
    print('Interação: ' + str(it))
    it = it + 1
    global at
    global pr
    global viz
    global res_viz
    at = [p[0], p[1], abs((p[0]) * np.sin((p[1]) * np.pi / 4) + (p[1]) * np.sin((p[0]) * np.pi / 4))]
    viz[0] = [(p[0] - 0.1), (p[1] - 0.1)]
    viz[1] = [(p[0] - 0.1), p[1]]
    viz[2] = [(p[0] - 0.1), (p[1] + 0.1)]
    viz[3] = [p[0], (p[1] - 0.1)]
    viz[4] = [p[0], (p[1] + 0.1)]
    viz[5] = [(p[0] + 0.1), (p[1] - 0.1)]
    viz[6] = [(p[0] + 0.1), p[1]]
    viz[7] = [(p[0] + 0.1), (p[1] + 0.1)]
    pr = at
    i = 0
    print(at)
    while i < 8:
        if 0 < (viz[i][0]) < 20.1 and 0 < viz[i][1] < 20:
            res_viz[i] = [
                abs((viz[i][0]) * np.sin((viz[i][1]) * np.pi / 4) + (viz[i][1]) * np.sin((viz[i][0]) * np.pi / 4))]
        else:
            res_viz[i] = at[2]
        if res_viz[i] > at[2]:
            if res_viz[i] > pr[2]:
                pr = [viz[i][0], viz[i][1], res_viz[i][0]]
        i = i + 1
    if pr[2] > at[2]:
        f_pro([pr[0], pr[1]])
    return at


arq = open('log-Hillclibing.txt', 'w')
nt = 1
while nt <= 50:
    print("Inicio Tentativa "+str(nt)+"\n\n")
    arq.write("\nTentativa: "+str(nt)+"  ")
    res = f_pro([random.randrange(0, 20, 1), random.randrange(0, 20, 1)])
    arq.write("X: "+str(res[0])+"  |  Y: "+str(res[1])+"   |   R: "+str(res[2])+"\n")
    arq.write("")
    print("\nFim Tentativa "+str(nt)+"\n\n")
    nt = nt + 1
arq.close()

plt.show()
