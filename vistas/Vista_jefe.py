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


        # Conectar el evento de clic del botón cargar_PDF_2 al método cargar_pdf_2_clicked
        self.cargar_PDF_2.clicked.connect(self.cargar_pdf_2_clicked)

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

    def cargar_pdf_2_clicked(self):
        # Obtener la fila seleccionada
        selected_row = self.tableWidget.currentRow()

        if selected_row >= 0:
            documento = self.comboBox.currentText()
            incapacidades = obtener_incapacidades_jefe(documento)

            if 0 <= selected_row < len(incapacidades):
                id_incapacidad_index = 2 

                if 0 <= id_incapacidad_index < len(incapacidades[selected_row]):
                    id_incapacidad = incapacidades[selected_row][id_incapacidad_index]

                    if id_incapacidad is not None:
                        print(f"Incapacidad {id_incapacidad} fue enviada.")
                    else:
                        print("No se pudo encontrar la ID_Incapacidad para la fila seleccionada.")
                else:
                    print("El índice de ID_Incapacidad está fuera de rango para la fila seleccionada.")
            else:
                print("La fila seleccionada está fuera de rango.")
        else:
            print("Por favor, selecciona una fila antes de hacer clic en Cargar PDF 2.")




if __name__ == '__main__':
    app = QApplication([])
    window = Vista_jefe()
    window.show()
    app.exec_()
