from CobroIncapacidades.Observador import Observador

class Recepcionista:
    def recibir_incapacidad(self, incapacidad):
        print(f"Recibiendo incapacidad para {incapacidad.tipo}")
        
    def actualizar(self, mensaje):
        print(f"Recepcionista {self.nombre} recibió el siguiente mensaje: {mensaje}")

    def agregar_observador(self, Observador):
        self.observadores.append(Observador)

    def solicitar_pago(self, incapacidad):
        print(f"Recepcionista: Solicitando pago para la incapacidad de {incapacidad.tipo}.")
        self.notificar_observadores(incapacidad)