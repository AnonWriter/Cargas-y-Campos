from campos import Carga2D, RecorridoPlano, CampoElectricoPlano
from vec import Vector2D

import matplotlib.pyplot as plt
import numpy as np

def GraficarCampoElectrico2D(ax, plano, campo, cargas, escala=1, color='b'):
    for punto, vector in zip(plano, campo):
        ax.quiver(
            punto.elements[0],  # x component
            punto.elements[1],  # y component
            vector.elements[0],  # U component
            vector.elements[1],  # V component
            color=color,
            scale=escala,
            alpha=0.5
        )
    
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.plot(carga.vec.elements[0], carga.vec.elements[1], color=color_carga, marker='o')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title("Campo eléctrico en el plano")
    plt.grid(True)

def GraficarCampoElectricoEscalar2D(ax, plano, cargas, escala=1):
    # Crear una malla para el plano
    X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
    Z = np.zeros(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            punto = Vector2D(X[i, j], Y[i, j])  # Trabajamos en el plano 2D
            campo_total = 0
            for carga in cargas:
                r_vector = punto + carga.vec.scalarm(-1)
                r_mag = r_vector.norm()
                if r_mag != 0:
                    campo = carga.val / (r_mag ** 2)
                    campo_total += campo

            Z[i, j] = campo_total * 10 

    # Normalizar Z para el mapeo de colores
    Z_normalized = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))

    # Usar un mapa de colores para representar la magnitud del campo
    # Puedes elegir un mapa de colores diferente si lo prefieres
    c = ax.pcolormesh(X, Y, Z_normalized, cmap='viridis')

    # Agregar puntos representando las cargas
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.plot(carga.vec.elements[0], carga.vec.elements[1], color=color_carga, marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.axis('equal')
    plt.title("Campo eléctrico escalar en 2D con mapa de colores")