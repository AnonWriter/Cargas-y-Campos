import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from graf3D import GraficarCampoElectrico3D, GraficarCampoElectricoEscalar3D
from graf2D import GraficarCampoElectrico2D, GraficarCampoElectricoEscalar2D
from campos import RecorridoEspacio, CampoElectricoEspacio, Carga3D, \
    Carga2D, CampoElectricoPlano, RecorridoPlano

def Agregar2D():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())

        valor = float(entry_valor.get())
        nueva_carga = Carga2D(x, y, valor)
        cargas2D.append(nueva_carga)
        Actualizar2D()
    except ValueError:
        print("Formato de datos incorrecto.")

def Actualizar2D():
    ax.clear()
    plano = RecorridoPlano(-10, 10, -10, 10)
    campo = CampoElectricoPlano(plano, cargas2D)
    
    if modo_vectorial:
        GraficarCampoElectrico2D(ax, plano, campo, cargas2D, escala=25)
    else:
        GraficarCampoElectricoEscalar2D(ax, plano, cargas2D, escala=25)
    
    canvas.draw()

def Reiniciar2D():
    cargas2D.clear()
    Actualizar2D()

def CambiarModo2D():
    global modo_vectorial
    modo_vectorial = not modo_vectorial
    Actualizar2D()


def AgregarCarga3D():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        z = float(entry_z.get())

        valor = float(entry_valor.get())
        nueva_carga = Carga3D(x, y, z, valor)
        cargas3D.append(nueva_carga)
        Actualizar3D()
    except ValueError:
        print("Formato de datos incorrecto.")

def Actualizar3D():
    ax.clear()
    espacio = RecorridoEspacio(-4, 4, -4, 4, -4, 4)
    campo = CampoElectricoEspacio(espacio, cargas3D)
    if modo_vectorial:
        GraficarCampoElectrico3D(ax, espacio, campo, cargas3D, escala=0.5)
    else:
        GraficarCampoElectricoEscalar3D(ax, espacio, cargas3D, escala=0.5)
    
    canvas.draw()


def Reiniciar3D():
    cargas3D.clear()
    Actualizar3D()

def CambiarModo3D():
    global modo_vectorial
    modo_vectorial = not modo_vectorial
    Actualizar3D()

def CambiarModo():
    global modo_3D, ax
    modo_3D = not modo_3D
    ax.clear()
    fig.delaxes(ax)
    if modo_3D:
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.add_subplot(111)
    canvas.draw()
    Reiniciar()

def Reiniciar():
    if modo_3D:
        Reiniciar3D()
    else:
        Reiniciar2D()

#interfaz

modo_3D = True

root = tk.Tk()
cargas3D = []
cargas2D = []

fig = Figure(figsize=(5,4), dpi=100)
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

frame_agregar_carga = tk.Frame(root)
frame_agregar_carga.pack(side=tk.TOP, fill=tk.X)

entry_x = tk.Entry(frame_agregar_carga)
entry_x.pack(side=tk.LEFT)
entry_y = tk.Entry(frame_agregar_carga)
entry_y.pack(side=tk.LEFT)
entry_z = tk.Entry(frame_agregar_carga)
entry_z.pack(side=tk.LEFT)
entry_valor = tk.Entry(frame_agregar_carga)
entry_valor.pack(side=tk.LEFT)

btn_agregar = tk.Button(frame_agregar_carga, text="Agregar Carga", command=lambda: Agregar2D() if not modo_3D else AgregarCarga3D())
btn_agregar.pack(side=tk.LEFT)

btn_reiniciar = tk.Button(root, text="Reiniciar", command=Reiniciar)
btn_reiniciar.pack(side=tk.TOP)

modo_vectorial = True
btn_cambiar_modo_visual = tk.Button(root, text="Cambiar Modo Visual", command=lambda: CambiarModo2D() if not modo_3D else CambiarModo3D())
btn_cambiar_modo_visual.pack(side=tk.TOP)

btn_cambiar_modo = tk.Button(root, text="Cambiar Modo Dimension", command=CambiarModo)
btn_cambiar_modo.pack(side=tk.TOP)

root.mainloop()