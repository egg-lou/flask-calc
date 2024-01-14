class OhmsCalculator:
    def __init__(self, voltage=None, current=None, resistance=None, power=None):
        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        self.power = power
    
    def calculate_voltage(self):
        if self.current is not None and self.resistance is not None:
            self.voltage = self.current * self.resistance
            return self.voltage
        else:
            return None

    def calculate_current(self):
        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            return self.current
        else:
            return None

    def calculate_resistance(self):
        if self.voltage is not None and self.current is not None:
            self.resistance = self.voltage / self.current
            return self.resistance
        else:
            return None
        
    def calculate_power(self):
        if self.voltage is not None and self.current is not None and self.power is None:
            self.power = self.voltage * self.current
            return self.power
        else:
            return None