from campos import Carga3D, RecorridoEspacio, CampoElectricoEspacio
from vec import Vector2D, Vector3D
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

import numpy as np

def GraficarCampoElectrico3D(ax, espacio, campo, cargas, escala=1, color='b'):
    for punto, vector in zip(espacio, campo):
        ax.quiver(
            punto.elements[0],
            punto.elements[1],
            punto.elements[2],
            vector.elements[0],
            vector.elements[1],
            vector.elements[2],
            color=color,
            length=escala,
            normalize=True,
            alpha=0.5
        )
    
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.scatter(carga.vec.elements[0], carga.vec.elements[1], carga.vec.elements[2], color=color_carga, s=100)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title("Campo electrico en el espacio")

def GraficarCampoElectricoEscalar3D(ax, espacio, cargas, escala=1):
    # Crear una malla para la superficie
    X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
    Z = np.zeros(X.shape)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            punto = Vector3D(X[i, j], Y[i, j], 0)  # Suponiendo que trabajamos en el plano Z=0
            campo_total = 0
            for carga in cargas:
                r_vector = punto + carga.vec.scalarm(-1)
                r_mag = r_vector.norm()
                if r_mag != 0:
                    campo = carga.val / (r_mag ** 2)
                    campo_total += campo

            Z[i, j] = campo_total

    # Normalizar Z para el coloreado
    Z_normalized = (Z - np.min(Z)) / (np.max(Z) - np.min(Z))

    # Usar el color para representar la magnitud del campo
    surface = ax.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(Z_normalized), alpha=1)

    # Agregar puntos representando las cargas
    for carga in cargas:
        color_carga = 'g' if carga.val > 0 else 'r'
        ax.scatter(carga.vec.elements[0], carga.vec.elements[1], 0, color=color_carga, s=100)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Magnitud del campo')
    plt.title("Campo eléctrico escalar en el espacio")