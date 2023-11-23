
from CobroIncapacidades.Recepcionista import Recepcionista
from CobroIncapacidades.AuxiliarAdministrativo import AuxiliarAdministrativo
from CobroIncapacidades.EPS_ARL import EPS_ARL
from CobroIncapacidades.SeguimientoCobro import SeguimientoCobro
from conciliacioncontable.ConcreteObserver import ConcreteObserver
from conciliacioncontable.ConcreteSubject import ConcreteSubject
from Incapacidad import Incapacidad

# Implementación del Patrón de Observador
class CobroFacade:
    def __init__(self):
        self.recepcionista = Recepcionista()
        self.auxiliar_administrativo = AuxiliarAdministrativo()
        self.eps_arl = EPS_ARL()
        self.seguimiento_cobro = SeguimientoCobro()
        self.conciliacion_subject = ConcreteSubject()
        self.conciliacion_observer = ConcreteObserver(self.conciliacion_subject, "ConciliacionObserver")

        # Agregar observadores
        self.recepcionista.agregar_observador(self.auxiliar_administrativo)
        self.recepcionista.agregar_observador(self.eps_arl)
        self.recepcionista.agregar_observador(self.seguimiento_cobro)

    def solicitar_pago(self, incapacidad):
        # Código para solicitar el pago y realizar el seguimiento
        print(f"Solicitando pago para la incapacidad: {incapacidad.tipo}")
        self.auxiliar_administrativo.solicitar_pago(incapacidad)
        self.eps_arl.solicitar_pago(incapacidad)
        self.seguimiento_cobro.realizar_seguimiento(incapacidad)

        # Después de realizar el seguimiento, notificar a la conciliación
        self.conciliacion_subject.notify()

# Ejemplo de uso 
facade = CobroFacade()

incapacidad = Incapacidad("Enfermedad General")

facade.solicitar_pago(incapacidad)
