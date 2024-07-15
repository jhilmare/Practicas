import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import tkinter as tk
from tkinter import ttk

# Clase base para las superficies 3D
class Superficie3D:
    def __init__(self, x_range, y_range):
        self.x_range = x_range
        self.y_range = y_range
        self.x, self.y = np.meshgrid(np.linspace(x_range[0], x_range[1], 100), 
                                     np.linspace(y_range[0], y_range[1], 100))

    def calcular_z(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    def generar_datos(self):
        self.z = self.calcular_z()
        return self.x, self.y, self.z

# Subclase para Plano
class Plano(Superficie3D):
    def __init__(self, x_range, y_range, pendiente):
        super().__init__(x_range, y_range)
        self.pendiente = pendiente

    def calcular_z(self):
        return self.pendiente * self.x

# Subclase para Paraboloide
class Paraboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        super().__init__(x_range, y_range)
        self.coef = coef

    def calcular_z(self):
        return self.coef * (self.x**2 + self.y**2)

# Subclase para Sinusoide
class Sinusoide(Superficie3D):
    def __init__(self, x_range, y_range, frecuencia):
        super().__init__(x_range, y_range)
        self.frecuencia = frecuencia

    def calcular_z(self):
        return np.sin(self.frecuencia * np.sqrt(self.x**2 + self.y**2))

# Subclase para Hiperboloide
class Hiperboloide(Superficie3D):
    def __init__(self, x_range, y_range, coef):
        super().__init__(x_range, y_range)
        self.coef = coef

    def calcular_z(self):
        return self.coef * (self.x**2 - self.y**2)

# Clase para visualizar superficies usando Matplotlib
class Visualizador3D:
    def __init__(self, superficie):
        self.superficie = superficie

    def mostrar_con_matplotlib(self):
        x, y, z = self.superficie.generar_datos()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap='viridis')
        plt.show()

# Clase para visualizar superficies usando Plotly
class Visualizador3DPlotly(Visualizador3D):
    def mostrar_con_plotly(self):
        x, y, z = self.superficie.generar_datos()
        fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        fig.update_layout(title='Superficie 3D', autosize=False, width=800, height=800)
        fig.show()

# Interfaz de usuario mejorada con Tkinter
def mostrar_interfaz():
    def seleccionar_superficie():
        tipo = combo_tipo.current()
        try:
            param = float(entry_parametro.get())
            if tipo == 0:
                superficie = Plano((-5, 5), (-5, 5), param)
            elif tipo == 1:
                superficie = Paraboloide((-5, 5), (-5, 5), param)
            elif tipo == 2:
                superficie = Sinusoide((-5, 5), (-5, 5), param)
            elif tipo == 3:
                superficie = Hiperboloide((-5, 5), (-5, 5), param)
            else:
                print("Opción no válida.")
                return

            visualizador = Visualizador3DPlotly(superficie)
            visualizador.mostrar_con_plotly()
        except ValueError:
            print("Ingrese un valor numérico válido.")

    root = tk.Tk()
    root.title("Selector de Superficies 3D")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label_tipo = ttk.Label(frame, text="Seleccione el tipo de superficie:")
    label_tipo.grid(row=0, column=0, columnspan=2)

    combo_tipo = ttk.Combobox(frame, values=["Plano", "Paraboloide", "Sinusoide", "Hiperboloide"])
    combo_tipo.grid(row=1, column=0, columnspan=2)

    label_parametro = ttk.Label(frame, text="Ingrese el parámetro correspondiente:")
    label_parametro.grid(row=2, column=0, columnspan=2)

    entry_parametro = ttk.Entry(frame)
    entry_parametro.grid(row=3, column=0, columnspan=2)

    boton_seleccionar = ttk.Button(frame, text="Generar Superficie", command=seleccionar_superficie)
    boton_seleccionar.grid(row=4, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    mostrar_interfaz()
