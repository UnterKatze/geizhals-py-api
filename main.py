import re
import requests
from enums import BaseURL, Currencies, CathegoryKeywords

# cat string
CATHEGORY_STR = "?cat="


def get_currency_from_str(price_str: str) -> str:
    for currency in Currencies:
        if currency.value in price_str:
            return currency.name
    return Currencies.UNKNOWN.name


def get_price_numeric(entry_price: str) -> str:
    price_numeric = re.sub("[^\d\.\,]", "", entry_price)
    price_numeric = re.sub("[\,]", ".", price_numeric)
    return price_numeric


class GeizhalsPyAPI:
    def __init__(self, baseURL: str = BaseURL.DE_DOMAIN.value):
        self.baseURL = baseURL

    def get_most_popular_cathegory_entries(self, cat: str, nr_of_entries: int = 10):
        url = self.baseURL + CATHEGORY_STR + cat
        resp = requests.get(url)
        html_cont = resp.text
        entries = {}
        if nr_of_entries <= 0 or nr_of_entries > 30:
            raise Exception("Can't search zero or less. Max entry number is 30.")
        for i in range(nr_of_entries):
            entry_str = html_cont.split(f'id="product{i}"')[-1].split(
                f'id="product{i + 1}"'
            )[0]
            entry_name = entry_str.split('data-name="')[-1].split('"')[0]
            entry_price = (
                entry_str.split('<span class="gh_price">')[-1]
                .split("</span>")[0]
                .split("<span class=notrans>")[-1]
            )
            currency = get_currency_from_str(entry_price)
            entry_price_numeric = get_price_numeric(entry_price)
            entry = {
                "item": entry_name,
                "price": entry_price_numeric,
                "currency": currency,
            }
            entries[i] = entry
        return entries


# set domain to DE
BASE_URL = BaseURL.DE_DOMAIN.value

# set Cathegory Keyword
CATH = CathegoryKeywords.CPU_AMD.value

if __name__ == "__main__":
    ghAPI = GeizhalsPyAPI(baseURL=BASE_URL)
    response = ghAPI.get_most_popular_cathegory_entries(cat=CATH, nr_of_entries=10)
    for key in response:
        print(response[key])
