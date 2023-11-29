from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from vistas.Vista_Login import *
from BaseDatos.connetion import *

class Vista_jefe(QMainWindow):
    def __init__(self):
        super(Vista_jefe, self).__init__()
        loadUi("vistas/PyQt5/vistaJefe.ui", self) 
        self.setWindowTitle("Gestor de incapacidades")
        
        incapacidades_data = obtener_incapacidades_jefe()
        # print(incapacidades_data)
        
        # Llena la QTableWidget con los datos obtenidos
        self.llenar_table_incapacidades(incapacidades_data)
        
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
