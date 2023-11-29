from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Registro import *
from vistas.vistaColaborador import *
from BaseDatos.connetion import *
from PyQt5.QtCore import QCoreApplication
from vistas.Vista_jefe import *

class VistaAuxiliarReporte(QMainWindow):
    def __init__(self):
        super(VistaAuxiliarReporte, self).__init__()
        loadUi("vistas/PyQt5/VistaAuxiliarReportes.ui", self) 
        self.setWindowTitle("Reportes Auxiliar Administrador")
        