
class Recepcionista:
    def recibir_incapacidad(self, incapacidad):
        print(f"Recibiendo incapacidad para {incapacidad.tipo}")
        
    def actualizar(self, mensaje):
        print(f"Recepcionista {self.nombre} recibió el siguiente mensaje: {mensaje}")