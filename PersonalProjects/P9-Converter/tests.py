# currencies = ["EUR", "USD", "PLN", "GBP", "CHF", "GBP", "CNH", "HKD", "JPY", "NOK", "HUF"]

# no_match = []
# cdB = []
# for i in range(len(currencies)):
#         for j in range(len(currencies)):
#             new_comb = currencies[i] + "/" + currencies[j]
#             if currencies[i] == currencies[j]:
#                 continue
#             elif new_comb not in cdB:
#                 cdB.append(new_comb)

# print(cdB, len(cdB))


units = ["km", "m", "dm", "cm", "mm", "in", "ft", "yd", "mi"]

lRates = {}
for i in range(len(units)):
        for j in range(len(units)):
            new_comb = units[i] + "/" + units[j]
            rev_comb = units[j] + "/" + units[i]
            if units[i] == units[j]:
                continue
            elif rev_comb in lRates:
                continue
            elif new_comb not in lRates:
                lRates[new_comb] = ''

print(lRates, len(lRates))

lRates = {'km/m': 10**3, 'km/dm': 10**4, 'km/cm': 10**5, 'km/mm': 10**6, 'km/in': 39370.0787, 'km/ft': 3280.8399,
          'km/yd': 1093.6133, 'km/mi': 0.621371192, 'm/dm': 10, 'm/cm': 100, 'm/mm': 10**3, 
          'm/in': 39.3700787, 'm/ft': 3.2808399, 'm/yd': 1.0936133, 'm/mi': 0.000621371192, 'dm/cm': 10, 
          'dm/mm': 100, 'dm/in': 3.93700787, 'dm/ft': 0.32808399, 'dm/yd': 0.10936133, 'dm/mi': 6.21371192*10**-5, 
          'cm/mm': 10, 'cm/in': 0.393700787, 'cm/ft': 0.032808399, 'cm/yd': 0.010936133, 'cm/mi': 6.21371192*10**-6, 
          'mm/in': 0.0393700787, 'mm/ft': 0.0032808399, 'mm/yd': 0.0010936133, 'mm/mi': 6.21371192*10**-7, 'in/ft': 0.0833333333, 
          'in/yd': 0.0277777778, 'in/mi': 1.57828283*10**-5, 'ft/yd': 0.333333333333333333, 'ft/mi': 0.000189393939, 
          'yd/mi': 0.000568181818}

        # elif rev_conversion in cdB.keys():
        #     rate = 1/cdB[rev_conversion]
        #     result = str(round(inputVal*rate,2))
        #     self.exchangeOutput.setText(result)

        # elif conversion not in cdB.keys() and rev_conversion not in cdB.keys() and check_USD in cdB.keys():#Convert to USD
        #     conversion = begCurr + "/USD"
        #     rev_conversion = "USD/" + begCurr

        #     if conversion in cdB.keys():
        #         rate = cdB[conversion]
        #         USD_result = (round(inputVal*rate,2))

        #         conversion = "USD/" + finCurr
        #         rev_conversion = finCurr + "/USD"

        #         if conversion in cdB.keys():
        #             rate = cdB[conversion]
        #             result = str(round(USD_result*rate,2))
        #             self.exchangeOutput.setText(result)

        #         elif rev_conversion in cdB.keys():
        #             rate = 1/cdB[rev_conversion]
        #             result = str(round(USD_result*rate,2))
        #             self.exchangeOutput.setText(result)

        #     elif rev_conversion in cdB.keys():
        #         rate = 1/cdB[rev_conversion]
        #         USD_result = (round(inputVal*rate,2))
                
        #         conversion = "USD/" + finCurr
        #         rev_conversion = finCurr + "/USD"

        #         if conversion in cdB.keys():
        #             rate = cdB[conversion]
        #             result = str(round(USD_result*rate,2))
        #             self.exchangeOutput.setText(result)

        #         elif rev_conversion in cdB.keys():
        #             rate = 1/cdB[rev_conversion]
        #             result = str(round(USD_result*rate,2))
        #             self.exchangeOutput.setText(result)