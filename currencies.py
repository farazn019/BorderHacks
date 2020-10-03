import requests


def currency():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/currencies"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "S915f3ed9fbmsha6957c677d44e14p1f10f3jsn323641387393"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


currency()
