
from CobroIncapacidades.Observador import Observador

class AuxiliarAdministrativo(Observador):
    def __init__(self):
        self.observadores = []
    def actualizar(self, incapacidad):
        print(f"Auxiliar Administrativo: Se ha recibido la solicitud de pago para la incapacidad de {incapacidad.tipo}.")
        self.realizar_pago()

    def realizar_pago(self):
        print("Auxiliar Administrativo: Realizando el proceso de pago.")
        
    def solicitar_pago(self, incapacidad):
        print(f"Auxiliar Administrativo: Solicitando pago para la incapacidad de {incapacidad.tipo}.")
        self.notificar_observadores(incapacidad)
        
    def notificar_observadores(self, incapacidad):
        for observador in self.observadores:
            observador.actualizar(incapacidad)
            
    def actualizar(self):
        pass
        
    
