from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import BaseDatos.connetion as BD

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("vistas/vistaColaborador.ui", self)
        self.show()
        
        documentacion = self.cargar_PDF.clicked.connect(self.show_file_dialog)
        self.Insertar.clicked.connect(lambda: self.insert_data(documentacion))
        self.Eliminar_PDF.clicked.connect(self.delete_pdf)
        
        self.llenar_tabla_incapacidades()
        
    def insert_data(self, documentacion):
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
        
        if (
            self.NamelineEdit.text() == "" or
            self.comboBox.currentText() == "Seleccionar" or
            self.DocumentLineEdit.text() == "" or
            self.comboBox_2.currentText() == "Seleccionar" or
            self.EmaillineEdit.text() == "" or
            self.ChargelineEdit.text() == "" or
            self.label_file_name.text() == "Seleccionar archivo..." or
            self.DescriptiontextEdit.toPlainText() == ""
        ):
            self.show_warning("Todos los campos deben estar llenos.")
            return
        
        type_document = self.show_selected_type_document()
        type_inability = self.show_selected_type_inability()
        selected_name = self.show_selected_name()
        selected_email = self.show_selected_email()
        selected_charge = self.show_selected_charge()
        selected_document = self.show_selected_document()
        # documentacion = self.show_file_dialog()
        
        BD.conectar()
        BD.insertar_colaborador(selected_charge, selected_document, selected_email, selected_name)
        BD.insertar_incapacidad(self.DescriptiontextEdit.toPlainText(), "Pendiente", selected_document, type_inability, documentacion, os.path.basename(self.label_file_name.text()))
        
    def show_selected_type_document(self):
        type_document = self.comboBox.currentText()
        # print(type_document)
        return type_document
        
    def show_selected_document(self):
        document = self.DocumentLineEdit.text()
        # print(document)
        return document
        
    def show_selected_type_inability(self):
        type_inability = self.comboBox_2.currentText()
        # print(type_inability)
        return type_inability
        
    def show_selected_name(self):
        name = self.NamelineEdit.text()
        # print(name)
        return name
        
    def show_selected_email(self):
        email = self.EmaillineEdit.text()
        # print(email)
        return email
        
    def show_selected_charge(self):
        charge = self.ChargelineEdit.text()
        # print(charge)
        return charge
        
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
            with open(file_name, "rb") as file:
                file_data = file.read()
            self.label_file_name.setText(file_name)
            return file_data
                
            
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
                QMessageBox.information(self, "Información", "Eliminación del archivo PDF cancelada.")
            
    def llenar_tabla_incapacidades(self):
        BD.conectar()
        incapacidades = BD.obtener_datos_incapacidades()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        
        # Llenar la tabla con los datos obtenidos
        for row_number, row_data in enumerate(incapacidades):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
            
        
        
def main():
    app = QApplication([])
    window = MyGUI()
    window.setWindowTitle("Gestión Incapacidades")
    app.exec_()

if __name__ == "__main__":
    main()