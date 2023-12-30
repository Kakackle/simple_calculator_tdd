import urllib.request
import json

from .main import SimpleCalculator

URL = ("https://data.nasa.gov/resource/y77d-th95.json")

# with urllib.request.urlopen(URL) as url:
#     data = json.loads(url.read().decode())

# masses = [float(d['mass']) for d in data if 'mass' in d]

# print(masses)

# calculator = SimpleCalculator()

# avg_mass = calculator.average(*masses)

# print(avg_mass)

class MeteoriteStats:
    def get_data(self):
        with urllib.request.urlopen(URL) as url:
            return json.loads(url.read().decode())

    def average_mass(self, data):
        calculator = SimpleCalculator()

        masses = [float(d['mass']) for d in data if 'mass' in d]

        return calculator.average(*masses)
