#class MainOffice
class MainOffice:
    def __init__(self):
        self.observadores = []
        
    def recibir_incapacidad(self, incapacidad):
        print(f"La Oficina Principal recibio incapacidad para {incapacidad.tipo}")
