from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from BaseDatos.connetion import *
from datetime import datetime

class AuxiliarWindow(QMainWindow):
    def __init__(self, email):
        super(AuxiliarWindow, self).__init__()
        uic.loadUi("vistas/vistaAuxiliar.ui", self)
        self.show()
        self.email = email  # Guardar el email en la instancia para su uso posterior

        # Conecta los botones a sus respectivas funciones
        self.cargar_PDF_3.clicked.connect(self.enviar_a_colaborador)
        self.cargar_PDF_2.clicked.connect(self.confirmar_transcripcion_arl)
        self.cargar_PDF_4.clicked.connect(self.confirmar_transcripcion_eps)
        self.pushButton.clicked.connect(self.generar_reporte_mensual)

        # Otros códigos de inicialización

    @pyqtSlot(str, str, str, str, str, str)
    def actualizar_informacion(self, nombre, tipo_documento, documento, tipo_incapacidad, email, descripcion):
        # Actualizar la interfaz con la nueva información
        self.labelincapacidades_5.setText(f"Nombre: {nombre}\n"
                                         f"Tipo de Documento: {tipo_documento}\n"
                                         f"Documento: {documento}\n"
                                         f"Tipo de Incapacidad: {tipo_incapacidad}\n"
                                         f"Email: {email}")
        self.DescriptiontextEdit_2.setPlainText(descripcion)

        # Consultar la base de datos y actualizar la tabla
        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Obtén el ID del colaborador usando el email almacenado en la instancia de la ventana
        ID_Colaborador = obtener_ID_colaborador(self.email)
    
        # Obtén los datos de incapacidades incluyendo el nombre del colaborador
        data_from_db = obtener_datos_incapacidades_con_nombre(ID_Colaborador)
    
        # Carga los datos en la tabla
        self.cargar_datos_en_tabla(data_from_db)

    def cargar_datos_en_tabla(self, data):
    # Limpia la tabla antes de cargar nuevos datos
        self.tableWidget_3.setRowCount(0)

        # Itera sobre los datos y agrégales a la tabla
        for row_number, row_data in enumerate(data):
            self.tableWidget_3.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                item = QTableWidgetItem(str(column_data))
                if isinstance(column_data, datetime):
                    formatted_date = column_data.strftime('%Y-%m-%d %H:%M:%S')
                    item.setText(formatted_date)
                    print(f"Fecha formateada: {formatted_date}")  # Agrega esta línea
                self.tableWidget_3.setItem(row_number, column_number, item)


    def enviar_a_colaborador(self):
        # Implementa la lógica para enviar la información faltante al colaborador
        pass

    def confirmar_transcripcion_arl(self):
        # Implementa la lógica para confirmar la transcripción a ARL
        pass

    def confirmar_transcripcion_eps(self):
        # Implementa la lógica para confirmar la transcripción a EPS
        pass

    def generar_reporte_mensual(self):
        # Implementa la lógica para generar el reporte mensual de incapacidades
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = AuxiliarWindow("correo_electronico@dominio.com")  # Reemplaza con el correo electrónico real
    window.setWindowTitle("Transcripción de Incapacidades")
    app.exec_()
