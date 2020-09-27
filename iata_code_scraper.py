import pycountry

number_countries = len(pycountry.countries)

country_lookup = "United Kingdom"

for country in range(number_countries):
    if list(pycountry.countries)[country].name == country_lookup:
        print("Found United Kingdom's code, it is: " + list(pycountry.countries)[country].alpha_2)

