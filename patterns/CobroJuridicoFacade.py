
from CobroJuridico.EPS import EPS
from CobroJuridico.ARL import ARL
from CobroJuridico.Cartera import Cartera
from CobroJuridico.AreaJuridica import AreaJuridica

class CobroJuridicoFacade:
    def __init__(self):
        self.eps = EPS()
        self.arl = ARL()
        self.cartera = Cartera()
        self.area_juridica = AreaJuridica()

        # Configurar la cadena de responsabilidad
        self.eps.set_next_handler(self.arl)
        self.arl.set_next_handler(self.cartera)
        self.cartera.set_next_handler(self.area_juridica)

    def gestionar_cobro_juridico(self, etapa):
        # Iniciar el proceso de cobro jurídico desde la etapa especificada
        self.eps.handle_request(etapa)

# Ejemplo de uso
facade = CobroJuridicoFacade()

facade.gestionar_cobro_juridico("Negación EPS")
