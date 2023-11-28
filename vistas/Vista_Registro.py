from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Login import *
from BaseDatos.connetion import *

class RegistroWindow(QDialog):
    def __init__(self):
        super(RegistroWindow, self).__init__()
        loadUi("vistas/Vista_Registro.ui", self)
        self.setWindowTitle("Registro")

        self.pushButton_3.clicked.connect(self.registrar)
        self.pushButton_4.clicked.connect(self.volver_a_login)

    def registrar(self):
        selected_charge = self.ChargelineEdit.text()
        selected_document = self.DocumentLineEdit.text()
        selected_email = self.EmaillineEdit.text()
        selected_name = self.NamelineEdit.text()
        selected_password = self.passwordLineEdit.text()
        selected_password_confirm = self.passwordLineEdit_2.text()
        #selected_password must be equals to selected_password_confirm
        
        # Base de Datos
        # Validación de Campos Obligatorios
        if not all([selected_charge, selected_document, selected_email, selected_name, selected_password, selected_password_confirm]):
            QMessageBox.warning(self, "Registro", "¡Todos los campos son obligatorios!")
            return
        
        # Validación de Contraseñas
        if selected_password != selected_password_confirm:
            QMessageBox.warning(self, "Registro", "¡Las contraseñas no coinciden!")
            return
        elif len(selected_password) < 8:  # Longitud mínima de contraseña
            QMessageBox.warning(self, "Registro", "¡La contraseña debe tener al menos 8 caracteres!")
            return
        
        try:
            if insertar_colaborador(selected_charge, selected_document, selected_email, selected_name, selected_password):
                QMessageBox.information(self, "Registro", "¡Usuario registrado exitosamente!")
                self.accept()
            else:
                QMessageBox.warning(self, "Registro", "¡El usuario ya existe!")
        except Exception as e:
            QMessageBox.warning(self, "Registro", f"¡Error al registrar usuario: {e}")

    def volver_a_login(self):
        self.reject()

if __name__ == "__main__":
    app = QApplication([])
    registro_window = RegistroWindow()
    registro_window.exec_()

