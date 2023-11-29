from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Login import *
from BaseDatos.connetion import *

class Vista_jefe(QMainWindow):
    def __init__(self):
        super(Vista_jefe, self).__init__()
        loadUi("vistas/PyQt5/vistaJefe.ui", self) 
        self.setWindowTitle("Gestor de incapacidades")
        
        self.fill_comboBox()
        self.comboBox.currentIndexChanged.connect(self.reload_table)
        
        notificacion = self.DescriptiontextEdit_2.toPlainText()
        
        self.enviarNoti.clicked.connect(lambda :self.enviar_notificacion(notificacion))
        self.textEdit.setText(obtener_mensajes(self.comboBox.currentText()))
        
        # print(incapacidades_data)
        
        # Llena la QTableWidget con los datos obtenidos
        
    def enviar_notificacion(self, notificacion):
        documento = self.comboBox.currentText()
        nombre = obtener_nombre_colaborador(documento)[0]
        self.label_2.setText("Notificación enviada a " + nombre)
        
        actualizar_mensajes(documento, notificacion)
        
    def reload_table(self):
        documento = self.comboBox.currentText()        
        incapacidades_data = obtener_incapacidades_jefe(documento)
        self.llenar_table_incapacidades(incapacidades_data)
        
    def fill_comboBox(self):
        colaboradores = obtener_colaboradores()
        documentos_unicos = set() 
        
        for colaborador in colaboradores:
            documento = colaborador[0]
            if documento not in documentos_unicos:
                self.comboBox.addItem(documento)
                documentos_unicos.add(documento)
        
    def llenar_table_incapacidades(self, incapacidades_data):
        self.tableWidget.setRowCount(len(incapacidades_data))
        self.tableWidget.setColumnCount(5)  # Ajusta según tus columnas

        # Llena la tabla con los datos
        for row_number, row_data in enumerate(incapacidades_data):
            for column_number, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                self.tableWidget.setItem(row_number, column_number, item)
                
if __name__ == '__main__':
    app = QApplication([])
    window = Vista_jefe()
    window.show()
    app.exec_()
