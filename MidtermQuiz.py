class TemperatureConversion:

    def __init__(self, ftemp=1, ktemp=2):
        self._ftemp = ftemp
        self._ktemp = ktemp


class FtoC(TemperatureConversion):

    def conversion(self):
        return ((self._ftemp-32)*5)/9.


tempinF = float(input("Enter the temperature in Fahrenheit: "))

convert = FtoC(tempinF)

print(str(convert.conversion()) + " Celsius")


class KtoC(TemperatureConversion):

    def conversion(self):
        return self._ktemp - 273.15


tempinK = float(input("Enter the temperature in Kelvin: "))

convert = KtoC(tempinK)

print(str(convert.conversion()) + " Celsius")