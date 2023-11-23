
# cobroincapacidades/Recepcionista.py
from CobroIncapacidades.Observador import Observador

class Recepcionista(Observador):
    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def solicitar_pago(self, incapacidad):
        print(f"Recepcionista: Solicitando pago para la incapacidad de {incapacidad.tipo}.")
        self.notificar_observadores(incapacidad)

