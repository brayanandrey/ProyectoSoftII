
from CobroIncapacidades.Observador import Observador

class EPS_ARL(Observador):
    def actualizar(self, incapacidad):
        print(f"EPS/ARL: Se ha recibido la solicitud de pago para la incapacidad de {incapacidad.tipo}.")
        self.procesar_pago()

    def procesar_pago(self):
        print("EPS/ARL: Procesando el pago de la incapacidad.")
        
    def solicitar_pago(self, incapacidad):
        pass
