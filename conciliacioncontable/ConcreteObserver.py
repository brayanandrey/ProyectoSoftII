# ConcreteObserver.py
from conciliacioncontable.PaymentObserver import PaymentObserver

class ConcreteObserver(PaymentObserver):
    def __init__(self, subject, name):
        self._subject = subject
        self._name = name

    def update(self):
        print(f"Observador {self._name} notificado del pago. Realizando conciliación.")
