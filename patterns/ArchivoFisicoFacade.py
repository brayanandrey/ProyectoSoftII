
from Incapacidad import Incapacidad
from archivoFisico.ArchivoFisicoRepository import ArchivoFisicoRepository

class ArchivoFisicoFacade:
    def __init__(self):
        self.archivo_fisico_repository = ArchivoFisicoRepository()

    def almacenar_incapacidad(self, incapacidad):
        self.archivo_fisico_repository.agregar_documento(incapacidad)
        print(f"Incapacidad almacenada en el archivo físico: {incapacidad.id}")

    def obtener_incapacidad_por_id(self, incapacidad_id):
        incapacidad = self.archivo_fisico_repository.obtener_documento_por_id(incapacidad_id)
        if incapacidad:
            print(f"Incapacidad encontrada: {incapacidad.nombre}")
        else:
            print(f"Incapacidad con ID {incapacidad_id} no encontrada.")

    def eliminar_incapacidad(self, incapacidad):
        self.archivo_fisico_repository.eliminar_documento(incapacidad)
        print(f"Incapacidad eliminada del archivo físico: {incapacidad.id}")

# Ejemplo de uso
if __name__ == "__main__":
    facade = ArchivoFisicoFacade()

    # Crear una incapacidad
    incapacidad = Incapacidad(id=1, nombre="Incapacidad123", tipo="Enfermedad General")

    # Almacenar la incapacidad en el archivo físico
    facade.almacenar_incapacidad(incapacidad)

    # Obtener la incapacidad por ID
    facade.obtener_incapacidad_por_id(1)

    # Eliminar la incapacidad
    facade.eliminar_incapacidad(incapacidad)
