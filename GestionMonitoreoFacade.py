
from Observable.Observable import ConcreteObservable
from Observable.Observer import ConcreteObserver1, ConcreteObserver2

class GestionMonitoreoFacade:
    def __init__(self):
        self.observable = ConcreteObservable()

    def monitorear_incapacidades(self, message):
        self.observable.notify(message)

# Ejemplo de uso
facade = GestionMonitoreoFacade()
observer1 = ConcreteObserver1()
observer2 = ConcreteObserver2()

facade.observable.attach(observer1)
facade.observable.attach(observer2)

facade.monitorear_incapacidades("Incapacidad vencida")
