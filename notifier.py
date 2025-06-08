from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class BasicNotifier(Notifier):
    def send(self, message):
        print(f"Notificación básica: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, wrappee):
        self._wrappee = wrappee

    def send(self, message):
        self._wrappee.send(message)

class EmailDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Enviando EMAIL: {message}")

class SMSDecorator(NotifierDecorator):
    def send(self, message):
        super().send(message)
        print(f"Enviando SMS: {message}")