
from registroBD.Incapacidad import Incapacidad
from registroBD.BaseDatos import BaseDatos

class RegistroBDFacade:
    def __init__(self):
        self.base_datos = BaseDatos()

    def almacenar_incapacidad(self, incapacidad):
        self.base_datos.agregar_incapacidad(incapacidad)
        print(f"Incapacidad almacenada en la base de datos: {incapacidad.id}")

    def obtener_incapacidad_por_id(self, incapacidad_id):
        incapacidad = self.base_datos.obtener_incapacidad_por_id(incapacidad_id)
        if incapacidad:
            print(f"Incapacidad encontrada: {incapacidad.nombre}")
        else:
            print(f"Incapacidad con ID {incapacidad_id} no encontrada.")

    def eliminar_incapacidad(self, incapacidad):
        self.base_datos.eliminar_incapacidad(incapacidad)
        print(f"Incapacidad eliminada de la base de datos: {incapacidad.id}")

# Ejemplo de uso
if __name__ == "__main__":
    facade = RegistroBDFacade()

    # Crear una incapacidad
    incapacidad = Incapacidad(id=1, nombre="Incapacidad123", tipo="Enfermedad General")

    # Almacenar la incapacidad en la base de datos
    facade.almacenar_incapacidad(incapacidad)

    # Obtener la incapacidad por ID
    facade.obtener_incapacidad_por_id(1)

    # Eliminar la incapacidad
    facade.eliminar_incapacidad(incapacidad)
