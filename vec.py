# funciones para los calculos y las funciones vectoriales
import numpy as np

class Vector2D:
    def  __init__(self, x1, x2): # inicializacion de un Vector2D
        self.elements = np.array([x1, x2])

    def __add__(self, other): # adicion vectorial simplificada
        return Vector2D(*(self.elements + other.elements))

    def scalarm(self, scalar): # multiplicacion vectorial simplificada
        return Vector2D(*(self.elements * scalar))

    def norm(self):
        return np.sqrt(self.elements[0]**2 + self.elements[1]**2)

    def __repr__(self): # representacion de par ordenado
        return f"Vector2D({self.elements[0]}, {self.elements[1]})"

class Vector3D:
    def  __init__(self, x1, x2, x3): # inicializacion de un Vector2D
        self.elements = np.array([x1, x2, x3])

    def __add__(self, other): # adicion vectorial simplificada
        return Vector3D(*(self.elements + other.elements))

    def scalarm(self, scalar): # multiplicacion vectorial simplificada
        return Vector3D(*(self.elements * scalar))

    def norm(self):
        return np.sqrt(self.elements[0]**2 + self.elements[1]**2 + self.elements[2]**2)

    def __repr__(self): # representacion de par ordenado
        return f"Vector3D({self.elements[0]}, {self.elements[1]}, {self.elements[2]})"

