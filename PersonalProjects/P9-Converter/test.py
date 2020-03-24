pRates = {"GPa/Pa":10**9, 
          "GPa/kPa":10**6, 
          "GPa/Mpa":10**3,
          "MPa/kPa":10**3
         }

if __name__ == "__main__":
    print(pRates.keys())

    if "GPa/Pa" in pRates.keys():
        print("Found")