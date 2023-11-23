from RecepcionIncapacidadesFacade import RecepcionIncapacidadesFacade
from Incapacidad import Incapacidad

facade = RecepcionIncapacidadesFacade()
incapacidad1 = Incapacidad("Enfermedad General")
incapacidad2 = Incapacidad("Accidente Laboral")

facade.recibir_incapacidad(incapacidad1)
facade.recibir_incapacidad(incapacidad2)

facade.verificar_incapacidades(incapacidad1)
facade.verificar_incapacidades(incapacidad2)
