import requests


def get_exchange_rates(currency='RON'):
    url = f"https://v6.exchangerate-api.com/v6/bde601172237e44c353583b4/latest/{currency}/"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rates", {})
