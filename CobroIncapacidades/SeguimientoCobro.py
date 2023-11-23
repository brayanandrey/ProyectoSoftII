
from CobroIncapacidades.Observador import Observador
from Incapacidad import Incapacidad

class SeguimientoCobro(Observador):
    def actualizar(self, incapacidad):
        print(f"SeguimientoCobro: Actualización de seguimiento de cobro para la incapacidad de {incapacidad.tipo}.")
