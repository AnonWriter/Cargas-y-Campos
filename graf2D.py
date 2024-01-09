from campos import Carga2D, RecorridoPlano, CampoElectricoPlano

import matplotlib.pyplot as plt
import numpy as np

def GraficarCampoElectrico2D(plano, campo, cargas, escala=1, color='b'):
    fig, ax = plt.subplots()

    for punto, vector in zip(plano, campo):
        ax.quiver(punto.elements[0], punto.elements[1], vector.elements[0], vector.elements[1], color=color, scale=escala)
    
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.plot(carga.vec.elements[0], carga.vec.elements[1], color=color_carga, marker='o')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title("Campo electrico")
    plt.grid(True)
    plt.show()

cargas = [
    Carga2D(3, 1, 1),
    Carga2D(-1, -3, -1)
]

x1, x2, y1, y2 = -5, 5, -5, 5
plano = RecorridoPlano(x1, x2, y1, y2)
campo = CampoElectricoPlano(plano, cargas)

GraficarCampoElectrico2D(plano, campo, cargas, escala=100)