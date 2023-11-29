from patterns.RecepcionIncapacidadesFacade import RecepcionIncapacidadesFacade
from patterns.RecepcionIncapacidadesFacade import RecepcionIncapacidadesFacade
from receptionMechanisms.LideresComerciales import LideresComerciales
from Incapacidad import Incapacidad
from GestionHumana import *
from vistas.vistaColaborador import *
from vistas.Vista_Login import *
from vistas.Vista_Registro import *
from vistas.vistaAuxiliar import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import os


def tipos_incapacidades():
    print("1. Enfermedad General")
    print("2. Accidente Laboral")
    print("3. Maternidad")
    print("4. Enfermedad Profesional")
    print("5. Accidente de Trabajo")
    print("6. Enfermedad Laboral")
    

def main():
    facade = RecepcionIncapacidadesFacade()


    facade.recibir_incapacidad(incapacidad1)
    facade.recibir_incapacidad(incapacidad2)

    facade.verificar_incapacidades(incapacidad1)
    facade.verificar_incapacidades(incapacidad2)

def obtener_incapacidad():
    tipo = input("Ingrese el tipo de incapacidad: ")
    incapacidad = Incapacidad(tipo)
    return incapacidad

# main.py

def exec_auxiliar_window(email):
    app = QApplication([])
    auxiliar_window = AuxiliarWindow(email)
    auxiliar_window.actualizar_informacion("nombre", "tipo_documento", "documento", "tipo_incapacidad", email, "descripcion")
    
    # Supongamos que obtienes la información necesaria para actualizar desde algún lugar
    nombre = "Nombre Colaborador"
    tipo_documento = "Cédula"
    documento = "123456789"
    tipo_incapacidad = "Enfermedad General"
    descripcion = "Descripción de la incapacidad"

    # Llama al método con la información necesaria
    auxiliar_window.actualizar_informacion(nombre, tipo_documento, documento, tipo_incapacidad, email, descripcion)

    auxiliar_window.show()
    app.exec_()

def exec_main_window():
    app = QApplication([])
    login_window = LoginWindow()

    if login_window.exec_() == QDialog.Accepted:
        email = login_window.obtener_email()
        main_window = MyGUI(email)
        main_window.setWindowTitle("Gestión Incapacidades")
        main_window.show()
        app.exec_()
        exec_auxiliar_window(email) 

def main():
    recepcion_facade = RecepcionIncapacidadesFacade()

    lideres_comerciales = LideresComerciales()

    colaborador_id = 123 
    tipo_incapacidad = "Enfermedad General"

    print(f"Colaborador {colaborador_id} llega a la empresa...")

    recepcionista_presente = True

    if recepcionista_presente:
        print("La recepcionista está presente.")
        incapacidad = Incapacidad(tipo_incapacidad)
        recepcion_facade.recibir_incapacidad(incapacidad)
    else:
        print("La recepcionista no está presente. Entregando directamente al proceso de Gestión Humana.")
        incapacidad = Incapacidad(tipo_incapacidad)
        recepcion_facade.entregar_directo_gestion_humana(incapacidad)

    print("Entregando en las oficinas principales y notificando a Gestión Humana...")

    auxiliares_presentes = True 

    if auxiliares_presentes:
        print("Auxiliares administrativas presentes. Entregando documentación y notificando a Gestión Humana.")
      
    print("Realizando otras acciones o procesos después de la entrega de la incapacidad.")

if __name__ == "__main__":
    #main()
    exec_main_window()