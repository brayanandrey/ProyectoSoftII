from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Registro import *
from vistas.vistaColaborador import *
from BaseDatos.connetion import *
from PyQt5.QtCore import QCoreApplication
from vistas.Vista_jefe import *

class Vista_Financiero(QMainWindow):
    def __init__(self):
        super(Vista_Financiero, self).__init__()
        loadUi("vistas/PyQt5/vistaFinanciero.ui", self) 
        self.setWindowTitle("vista financiero")
        
    