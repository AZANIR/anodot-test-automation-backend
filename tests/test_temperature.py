from pytemp import pytemp


class TestСonversion:

    # Test conversion from fahrenheit to celsius and back
    def test_fahrenheit_to_celsius_and_back(self):
        fahrenheit = pytemp(32, 'f', 'c')
        assert round(fahrenheit, 2) == 0.00
        fahrenheit = pytemp(212, 'f', 'c')
        assert round(fahrenheit, 2) == 100.00
        celsius = pytemp(0, 'c', 'f')
        assert round(celsius, 2) == 32.00
        celsius = pytemp(100, 'c', 'f')
        assert round(celsius, 2) == 212.00

    # Test conversion from kelvin to celsius and back
    def test_kelvin_to_celsius_and_back(self):
        kelvin = pytemp(273.15, 'k', 'c')
        assert round(kelvin, 2) == 0.00
        kelvin = pytemp(373.15, 'k', 'c')
        assert round(kelvin, 2) == 100.00
        celsius = pytemp(0, 'c', 'k')
        assert round(celsius, 2) == 273.15
        celsius = pytemp(100, 'c', 'k')
        assert round(celsius, 2) == 373.15

    # Test conversion from kelvin to fahrenheit and back
    def test_kelvin_to_fahrenheit_and_back(self):
        fahrenheit = pytemp(273.15, 'k', 'f')
        assert round(fahrenheit, 2) == 32.00
        fahrenheit = pytemp(373.15, 'k', 'f')
        assert round(fahrenheit, 2) == 212.00
        kelvin = pytemp(32, 'f', 'k')
        assert round(kelvin, 2) == 273.15
        kelvin = pytemp(212, 'f', 'k')
        assert round(kelvin, 2) == 373.15
