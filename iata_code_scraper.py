import pycountry


def country_code(country_name):
    number_countries = len(pycountry.countries)

    for country in range(number_countries):
        if list(pycountry.countries)[country].name == country_name:
            code = list(pycountry.countries)[country].alpha_2
            print("Found the country code for " + country_name + ". It is, " + code)

    return code

