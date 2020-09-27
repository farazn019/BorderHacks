import pycountry


def country_code(country_name):
    number_countries = len(pycountry.countries)

    # country_lookup = "United Kingdom"

    for country in range(number_countries):
        if list(pycountry.countries)[country].name == country_name:
            print("Found the country code for " + country_name + ". It is, "+list(pycountry.countries)[country].alpha_2)

