
class GestionHumana:
    def recibir_incapacidad_directa(self, incapacidad):
        print(f"Proceso de Gestión Humana recibe incapacidad directa para {incapacidad.tipo}")
    
    def entregar_directo_gestion_humana(self, incapacidad):
        gestion_humana = GestionHumana() 
        gestion_humana.recibir_incapacidad_directa(incapacidad)
