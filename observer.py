from abc import ABC, abstractmethod
from logger import Logger

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temperature):
        self._temperature = temperature
        Logger().log(f"Nueva temperatura: {temperature}°C")
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

class TempDisplay(Observer):
    def update(self, temperature):
        print(f"Pantalla muestra temperatura: {temperature}°C")

class AlertService(Observer):
    def __init__(self, notifier):
        self.notifier = notifier

    def update(self, temperature):
        if temperature > 30:
            message = f"¡Temperatura alta: {temperature}°C!"
            self.notifier.send(message)
            Logger().log("Alerta enviada por alta temperatura.")