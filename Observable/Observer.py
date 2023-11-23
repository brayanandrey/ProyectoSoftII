
class Observer:
    def update(self, message):
        pass

class ConcreteObserver1(Observer):
    def update(self, message):
        print(f"Observer 1 received: {message}")

class ConcreteObserver2(Observer):
    def update(self, message):
        print(f"Observer 2 received: {message}")
