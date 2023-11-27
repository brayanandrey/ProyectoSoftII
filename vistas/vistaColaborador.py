from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("vistas/vistaColaborador.ui", self)
        self.show()
        
        self.Insertar.clicked.connect(self.insert_data)
        self.cargar_PDF.clicked.connect(self.show_file_dialog)
        self.Eliminar_PDF.clicked.connect(self.delete_pdf)
        
    def insert_data(self):
        #Compare text diferent of null or empty string
        if self.NamelineEdit.text() == "":
            self.show_warning("El campo de nombre no puede estar vacío.")
            return
        if self.comboBox.currentText() == "Seleccionar":
            self.show_warning("Debe seleccionar un tipo de documento.")
            return
        if self.DocumentLineEdit.text() == "":
            self.show_warning("El campo de documento no puede estar vacío.")
            return
        if self.comboBox_2.currentText() == "Seleccionar":
            self.show_warning("Debe seleccionar un tipo de incapacidad.")
            return
        if self.EmaillineEdit.text() == "":
            self.show_warning("El campo de email no puede estar vacío.")
            return
        if self.ChargelineEdit.text() == "":
            self.show_warning("El campo de cargo no puede estar vacío.")
            return
        
        if self.label_file_name.text() == "Seleccionar archivo...":
            self.show_warning("Debe cargar un archivo PDF.")
            return

        if self.DescriptiontextEdit.toPlainText() == "":
            self.show_warning("El campo de descripción no puede estar vacío.")
            return
        
        
        self.show_selected_type_document()
        self.show_selected_type_inability()
        self.show_selected_name()
        self.show_selected_email()
        self.show_selected_charge()
        
    def show_selected_type_document(self):
        type_document = self.comboBox.currentText()
        print(type_document)
        
    def show_selected_document(self):
        type_document = self.DocumentLineEdit.currentText()
        print(type_document)
        
    def show_selected_type_inability(self):
        type_inability = self.comboBox_2.currentText()
        print(type_inability)
        
    def show_selected_name(self):
        name = self.NamelineEdit.text()
        print(name)
        
    def show_selected_email(self):
        email = self.EmaillineEdit.text()
        print(email)
        
    def show_selected_charge(self):
        charge = self.ChargelineEdit.text()
        print(charge)
        
    def show_warning(self, message):
        QMessageBox.warning(self, "Advertencia", message)

        
    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PDF (*.pdf)")
        
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_name = file_dialog.selectedFiles()[0]
            print(file_name)
            self.label_file_name.setText(file_name)
            
    def delete_pdf(self):
        current_file = self.label_file_name.text()
        
        if current_file != "Seleccionar archivo...":
            reply = QMessageBox.question(self, 'Eliminar PDF', '¿Está seguro de que desea eliminar el PDF actual?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                os.remove(current_file)
                self.label_file_name.setText("Seleccionar archivo...")
                QMessageBox.information(self, "Información", "El archivo PDF ha sido eliminado.")
            else:
                QMessageBox.information(self, "Información", "Eliminación dek archivo PDF cancelada.")
            
            
            
        
        
def main():
    app = QApplication([])
    window = MyGUI()
    window.setWindowTitle("Gestión Incapacidades")
    app.exec_()

if __name__ == "__main__":
    main()