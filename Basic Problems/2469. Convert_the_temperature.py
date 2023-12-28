from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp = []

        # Convert Celsius to Kelvin using the formula: Kelvin = Celsius + 273.15
        kelvin_values = celsius + 273.15
        temp.append(kelvin_values)

        # Convert Celsius to Fahrenheit using the formula: Fahrenheit = Celsius * 1.80 + 32.00
        fahrenheit_values = celsius * 1.80 + 32.00
        temp.append(fahrenheit_values)

        return temp 