
pRates = {"GPa/Pa":10**9, 
          "GPa/hPa":10**7,
          "GPa/kPa":10**6, 
          "GPa/MPa":10**3,
          "MPa/Pa":10**6,
          "MPa/hPa":10**4,
          "MPa/kPa":10**3,
          "kPa/Pa":10**3,
          "kPa/hPa":10,
          "hPa/Pa":10**2,
          "atm/GPa":0.000101325,
          "atm/MPa":0.101325,
          "atm/kPa":101.325,
          "atm/hPa":1013.25,
          "atm/Pa":101325,
          "Bar/GPa":0.0001,
          "Bar/MPa":0.1,
          "Bar/kPa":100,
          "Bar/hPa":1000,
          "Bar/Pa":100000,
          "mBar/GPa":10**-6,
          "mBar/MPa":0.0001,
          "mBar/kPa":0.1,
          "mBar/hPa":1,
          "mBar/Pa":100,
          "mBar/Bar":0.001,
          "mBar/atm":0.000986923267,
          "Bar/atm":0.986923267
         }

lRates = {'km/m': 10**3, 'km/dm': 10**4, 'km/cm': 10**5, 'km/mm': 10**6, 'km/in': 39370.0787, 'km/ft': 3280.8399,
          'km/yd': 1093.6133, 'km/mi': 0.621371192, 'm/dm': 10, 'm/cm': 100, 'm/mm': 10**3, 
          'm/in': 39.3700787, 'm/ft': 3.2808399, 'm/yd': 1.0936133, 'm/mi': 0.000621371192, 'dm/cm': 10, 
          'dm/mm': 100, 'dm/in': 3.93700787, 'dm/ft': 0.32808399, 'dm/yd': 0.10936133, 'dm/mi': 6.21371192*10**-5, 
          'cm/mm': 10, 'cm/in': 0.393700787, 'cm/ft': 0.032808399, 'cm/yd': 0.010936133, 'cm/mi': 6.21371192*10**-6, 
          'mm/in': 0.0393700787, 'mm/ft': 0.0032808399, 'mm/yd': 0.0010936133, 'mm/mi': 6.21371192*10**-7, 'in/ft': 0.0833333333, 
          'in/yd': 0.0277777778, 'in/mi': 1.57828283*10**-5, 'ft/yd': 0.333333333333333333, 'ft/mi': 0.000189393939, 
          'yd/mi': 0.000568181818}

if __name__ == "__main__":
    print(pRates.keys())
    key = "GPa/MPa"

    if key in pRates.keys():
        print(pRates[key])