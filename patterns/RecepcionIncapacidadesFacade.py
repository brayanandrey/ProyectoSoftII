import Incapacidad
from receptionMechanisms.MainOffices import MainOffices
from receptionMechanisms.Receptionista import *
from VerificadorIncapacidades import *

# Implementación del Patrón de Fachada
class RecepcionIncapacidadesFacade:
    def __init__(self):
        self.verificador = VerificadorIncapacidades()
        self.recepcionista = Recepcionista()

    def recibir_incapacidad(self, incapacidad):
        self.recepcionista.recibir_incapacidad(incapacidad)

    def verificar_incapacidades(self):
        self.verificador.verificar_incapacidades()
        

# Ejemplo de uso
facade = RecepcionIncapacidadesFacade()
incapacidad1 = Incapacidad("Enfermedad General")
incapacidad2 = Incapacidad("Accidente Laboral")

facade.recibir_incapacidad(incapacidad1)
facade.recibir_incapacidad(incapacidad2)

facade.verificar_incapacidades()