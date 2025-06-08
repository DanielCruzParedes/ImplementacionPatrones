```mermaid
classDiagram
  WeatherStation o-- " * " Observer
  Observer <|-- TempDisplay
  Observer <|-- AlertService
  class WeatherStation {
    - _observers: List~Observer~
    - _temperature: float
    + attach(o: Observer): void
    + set_temperature(t: float): void
    - notify_observers(): void
  }
  class Observer {
    <<interface>>
    + update(temperature: float): void
  }
  class TempDisplay {
    + update(temperature: float): void
  }
  class AlertService {
    - notifier: Notifier
    + update(temperature: float): void
  }
