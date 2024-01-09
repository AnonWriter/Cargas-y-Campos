from campos import Carga3D, RecorridoEspacio, CampoElectricoEspacio

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def GraficarCampoElectrico3D(espacio, campo, cargas, escala=1, color='b'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for punto, vector in zip(espacio, campo):
        ax.quiver(punto.elements[0], punto.elements[1], punto.elements[2], vector.elements[0], vector.elements[1], vector.elements[2], color=color, length=escala, normalize=True)
    
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.scatter(carga.vec.elements[0], carga.vec.elements[1], carga.vec.elements[2], color=color_carga, s=100)

    # ax.set_aspect('equal', 'box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title("Campo electrico en el espacio")
    # plt.grid(True)
    plt.show()

cargas = [
    Carga3D(2, 3, 1, 1),
    Carga3D(-1, -1, -1, -1)
]

x1, x2, y1, y2, z1, z2 = -3, 3, -3, 3, -3, 3
espacio = RecorridoEspacio(x1, x2, y1, y2, z1, z2)
campo = CampoElectricoEspacio(espacio, cargas)

GraficarCampoElectrico3D(espacio, campo, cargas, escala=0.5)