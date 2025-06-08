from notifier import BasicNotifier, EmailDecorator, SMSDecorator
from observer import WeatherStation, TempDisplay, AlertService
import pandas as pd
import numpy as np 

if __name__ == "__main__":

    np.random.seed()
    data = pd.DataFrame({
    "hora": pd.date_range(start="2025-06-01", periods=24, freq="H"),
    "temperatura": np.random.normal(loc=27, scale=5, size=24).round(1) 
    })

    station = WeatherStation()

    # Observadores
    display = TempDisplay()

    # Decoradores encadenados
    notifier = BasicNotifier()
    notifier = EmailDecorator(notifier)
    notifier = SMSDecorator(notifier)

    alert_service = AlertService(notifier)

    # Registrar observadores
    station.attach(display)
    station.attach(alert_service)

    # Simular cambio de temperatura
    for _, row in data.iterrows():
        station.set_temperature(row["temperatura"])
        print("---")