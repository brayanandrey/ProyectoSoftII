from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Registro import *
from vistas.vistaColaborador import *

class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("vistas/Vista_Login.ui", self) 
        self.setWindowTitle("Inicio de Sesión")

        self.pushButton.clicked.connect(self.abrir_registro)
        self.pushButton_2.clicked.connect(self.iniciar_sesion)

    def abrir_registro(self):
        registro_window = RegistroWindow()
        if registro_window.exec_() == QDialog.Accepted:
            self.reject()

    def iniciar_sesion(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # Base de Datos

        if email == "usu" and password == "1234":
            self.accept()
            main_window = MyGUI()
            main_window.show() 
        else:
            QMessageBox.warning(self, "Inicio de Sesión", "¡Autenticación fallida!")

if __name__ == "__main__":
    app = QApplication([])
    login_window = LoginWindow()
    login_window.exec_()