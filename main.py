from patterns.RecepcionIncapacidadesFacade import RecepcionIncapacidadesFacade
from patterns.RecepcionIncapacidadesFacade import RecepcionIncapacidadesFacade
from receptionMechanisms.LideresComerciales import LideresComerciales
from Incapacidad import Incapacidad
from GestionHumana import *
from vistas.vistaColaborador import *
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

def exec_window():
    app = QApplication([])
    window = MyGUI()
    window.setWindowTitle("Gestión Incapacidades")
    app.exec_()
    return window
    


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
    exec_window()

    
    