
from CobroIncapacidades.Observador import Observador

class AuxiliarAdministrativo(Observador):
    def actualizar(self, incapacidad):
        print(f"Auxiliar Administrativo: Se ha recibido la solicitud de pago para la incapacidad de {incapacidad.tipo}.")
        self.realizar_pago()

    def realizar_pago(self):
        print("Auxiliar Administrativo: Realizando el proceso de pago.")
