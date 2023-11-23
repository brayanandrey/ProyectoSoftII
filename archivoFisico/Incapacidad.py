
from archivoFisico.Documento import Documento

class Incapacidad(Documento):
    def __init__(self, id, nombre, tipo):
        super().__init__(id, nombre)
        self.tipo = tipo
