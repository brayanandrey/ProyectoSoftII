
# TranscripcionFacade.py
import Incapacidad
from receptionMechanisms.Receptionista import Recepcionista
from receptionMechanisms.VerificacionDocumental import VerificacionDocumental
from ContextoTranscripcion.TranscriptorARL import TranscriptorARL
from ContextoTranscripcion.TranscriptorEPS import TranscriptorEPS

class TranscripcionFacade:
    def __init__(self):
        self.recepcionista = Recepcionista()
        self.verificacion_documental = VerificacionDocumental()
        self.transcriptor_arl = TranscriptorARL()
        self.transcriptor_eps = TranscriptorEPS()

    def recibir_incapacidad(self, incapacidad):
        self.recepcionista.recibir_incapacidad(incapacidad)

    def verificar_documentacion(self, incapacidad):
        self.verificacion_documental.verificar_documentacion(incapacidad)

    def transcribir_incapacidad_arl(self, incapacidad):
        self.transcriptor_arl.transcribir(incapacidad)

    def transcribir_incapacidad_eps(self, incapacidad):
        self.transcriptor_eps.transcribir(incapacidad)

# Ejemplo de uso
facade = TranscripcionFacade()
incapacidad = Incapacidad("Enfermedad General")

facade.recibir_incapacidad(incapacidad)
facade.verificar_documentacion(incapacidad)
facade.transcribir_incapacidad_arl(incapacidad)
facade.transcribir_incapacidad_eps(incapacidad)

