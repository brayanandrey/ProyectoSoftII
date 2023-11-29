from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from BaseDatos.connetion import *

class VistaColaboradorObservaciones(QMainWindow):
    def __init__(self, ID_colaborador):
        super(VistaColaboradorObservaciones, self).__init__()
        loadUi("vistas/PyQt5/VistaColaboradorObservaciones.ui", self) 
        self.setWindowTitle("Observaciones de Colaborador")
        self.ID_colaborador = ID_colaborador

    def llenar_observaciones(self):
        try:
            # Tu lógica para llenar la ventana con observaciones
            print("Llenando observaciones")
        except Exception as e:
            print("Error:", e)

# ...

# En tu función donde abres la ventana
def abrir_observaciones(self):
    print("Abriendo observaciones")
    
    # Utiliza el atributo de la clase en lugar de una variable local
    self.ventana_observaciones = VistaColaboradorObservaciones(self.DocumentLineEdit.text())
    self.ventana_observaciones.show()  # Asegúrate de llamar a show() para hacer visible la ventana

        