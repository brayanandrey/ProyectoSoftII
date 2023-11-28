from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Registro import *
from vistas.vistaColaborador import *
from BaseDatos.connetion import *
from PyQt5.QtCore import QCoreApplication

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
            self.close() 
            # QCoreApplication.processEvents()

    def iniciar_sesion(self):
        email = self.Email_lineEdit.text()
        password = self.password_lineEdit.text()
        
        if (verificar_credenciales(email, password)):
            self.accept()
        else:
            QMessageBox.warning(self, "Inicio de Sesión", "¡Autenticación fallida!")
            return
    
    def obtener_email(self):
        return self.Email_lineEdit.text()

if __name__ == "__main__":
    app = QApplication([])
    login_window = LoginWindow()
    login_window.exec_()