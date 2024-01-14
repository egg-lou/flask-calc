class OhmsCalculator:
    """
    A class used to perform Ohm's Law calculations.

    ...

    Attributes
    ----------
    voltage : float
        the voltage in volts
    current : float
        the current in amperes
    resistance : float
        the resistance in ohms
    power : float
        the power in watts

    Methods
    -------
    calculate_voltage():
        Calculates the voltage using the current and resistance.
    calculate_current():
        Calculates the current using the voltage and resistance.
    calculate_resistance():
        Calculates the resistance using the voltage and current.
    calculate_power():
        Calculates the power using the voltage and current.
    """

    def __init__(self, voltage=None, current=None, resistance=None, power=None):
        """
        Constructs all the necessary attributes for the OhmsCalculator object.

        Parameters
        ----------
            voltage : float
                the voltage in volts
            current : float
                the current in amperes
            resistance : float
                the resistance in ohms
            power : float
                the power in watts
        """

        self.voltage = voltage
        self.current = current
        self.resistance = resistance
        self.power = power
    
    def calculate_voltage(self):
        """
        Calculates the voltage using the current and resistance.

        Returns
        -------
        float
            The calculated voltage in volts. If the current or resistance is None, returns None.
        """

        if self.current is not None and self.resistance is not None:
            self.voltage = self.current * self.resistance
            return self.voltage
        else:
            return None

    def calculate_current(self):
        """
        Calculates the current using the voltage and resistance.

        Returns
        -------
        float
            The calculated current in amperes. If the voltage or resistance is None, returns None.
        """

        if self.voltage is not None and self.resistance is not None:
            self.current = self.voltage / self.resistance
            return self.current
        else:
            return None

    def calculate_resistance(self):
        """
        Calculates the resistance using the voltage and current.

        Returns
        -------
        float
            The calculated resistance in ohms. If the voltage or current is None, returns None.
        """

        if self.voltage is not None and self.current is not None:
            self.resistance = self.voltage / self.current
            return self.resistance
        else:
            return None
        
    def calculate_power(self):
        """
        Calculates the power using the voltage and current.

        Returns
        -------
        float
            The calculated power in watts. If the voltage or current is None, returns None.
        """

        if self.voltage is not None and self.current is not None and self.power is None:
            self.power = self.voltage * self.current
            return self.power
        else:
            return None