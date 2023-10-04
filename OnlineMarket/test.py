import requests


def get_exchange_rates():
    url = "https://v6.exchangerate-api.com/v6/bde601172237e44c353583b4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rates", {})


# print(get_exchange_rates())
# print([[key, value] for key, value in get_exchange_rates().items()])
