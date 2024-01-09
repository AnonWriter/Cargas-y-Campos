# funciones para los calculos de campos
import numpy as np
from vec import Vector2D, Vector3D

class Carga2D:
    def __init__(self, x1, x2, q):
        self.vec = Vector2D(x1, x2)
        self.val = q

class Carga3D:
    def __init__(self, x1, x2, x3, q):
        self.vec = Vector3D(x1, x2, x3)
        self.val = q


def RecorridoPlano(x1, x2, y1, y2):
    plano = []

    total_x = abs(x1) + abs(x2)
    total_y = abs(y1) + abs(y2)

    for i in range(total_x):
        for j in range(total_y):
            vector = Vector2D(x1 + i, y1 + j)
            plano.append(vector)

    return plano

    
def RecorridoEspacio(x1, x2, y1, y2, z1, z2):
    espacio = []

    total_x = abs(x1) + abs(x2)
    total_y = abs(y1) + abs(y2)
    total_z = abs(z1) + abs(z2)

    for i in range(total_x):
        for j in range(total_y):
            for k in range(total_z):
                vector = Vector3D(x1 + i, y1 + j, z1 + k)
                espacio.append(vector)

    return espacio

def CampoElectricoPlano(plano, cargas2d):
    k_e = 8.9875517873681764 #constante de coulumb escalada para accesibilidad
    mcampo = 0 #magnitud del vector de campo
    campo = []
    for vector in plano:
        vector_campo = Vector2D(0,0)
        for q in cargas2d:
            r = Vector2D(0,0)

            if q.val < 0:
                r = q.vec + vector.scalarm(-1)
            else:
                r = vector + q.vec.scalarm(-1)
            
            if r.norm() != 0:
                mcampo = (k_e * abs(q.val)) / r.norm() ** 3
            else:
                mcampo = 0
            
            vector_campo += r.scalarm(mcampo)
        
        campo.append(vector_campo)
    
    return campo

def CampoElectricoEspacio(espacio, cargas3d):
    k_e = 1 #constante de coulumb escalada para accesibilidad
    mcampo = 0 #magnitud del vector de campo
    campo = []
    for vector in espacio:
        vector_campo = Vector3D(0,0,0)
        for q in cargas3d:
            r = Vector3D(0,0,0)

            if q.val < 0:
                r = q.vec + vector.scalarm(-1)
            else:
                r = vector + q.vec.scalarm(-1)
            
            if r.norm() != 0:
                mcampo = (k_e * abs(q.val)) / r.norm() ** 3
            else:
                mcampo = 0
            
            vector_campo += r.scalarm(mcampo)
        
        campo.append(vector_campo)
    
    return campo
