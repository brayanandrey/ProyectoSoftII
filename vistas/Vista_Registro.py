from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Login import *

class RegistroWindow(QDialog):
    def __init__(self):
        super(RegistroWindow, self).__init__()
        loadUi("vistas/Vista_Registro.ui", self)
        self.setWindowTitle("Registro")

        self.pushButton_3.clicked.connect(self.registrar)
        self.pushButton_4.clicked.connect(self.volver_a_login)

    def registrar(self):
        # Base de Datos
        QMessageBox.information(self, "Registro", "¡Usuario registrado exitosamente!")
        self.accept()

    def volver_a_login(self):
        self.reject()

if __name__ == "__main__":
    app = QApplication([])
    registro_window = RegistroWindow()
    registro_window.exec_()

