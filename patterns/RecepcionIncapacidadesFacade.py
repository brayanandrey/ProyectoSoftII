from Incapacidad import Incapacidad
from GestionHumana import *
from receptionMechanisms.MainOffices import *
from receptionMechanisms.Receptionista import *
from receptionMechanisms.Notificador import Notificador
from receptionMechanisms.VerificacionDocumental import *
from VerificadorIncapacidades import *
from receptionMechanisms.LideresComerciales import LideresComerciales

# Implementación del Patrón de Fachada
class RecepcionIncapacidadesFacade:
    def __init__(self):
        self.verificador = VerificadorIncapacidades()
        self.recepcionista = Recepcionista()
        self.notificador = Notificador()
        self.verificacion_documental = VerificacionDocumental()
        self.oficina_principal = MainOffice()
        self.lideres_comerciales = LideresComerciales()

    def recibir_incapacidad(self, incapacidad):
        self.recepcionista.recibir_incapacidad(incapacidad)
        self.notificador.notificar_recepcion(incapacidad)
        self.oficina_principal.recibir_incapacidad(incapacidad)
        self.lideres_comerciales.recibir_incapacidad(incapacidad)

    def verificar_incapacidades(self, incapacidad):
        self.verificador.verificar_incapacidades()
        self.notificador.notificar_verificacion()
        self.verificacion_documental.verificar_documentacion(incapacidad)
         

# Ejemplo de uso
if __name__ == "__main__":
    facade = RecepcionIncapacidadesFacade()
    incapacidad1 = Incapacidad("Enfermedad General")
    incapacidad2 = Incapacidad("Accidente Laboral")

    facade.recibir_incapacidad(incapacidad1)
    facade.recibir_incapacidad(incapacidad2)

    facade.verificar_incapacidades(incapacidad1)
    facade.verificar_incapacidades(incapacidad2)
