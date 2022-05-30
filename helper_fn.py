from helper_enums import Currencies
import re


def get_currency_from_str(price_str: str) -> str:
    for currency in Currencies:
        if currency.value in price_str:
            return currency.name
    return Currencies.UNKNOWN.name


def get_price_numeric(entry_price: str) -> float:
    price_numeric = re.sub("[^\d\.\,]", "", entry_price)
    price_numeric = re.sub("[\,]", ".", price_numeric)
    return float(price_numeric)


def get_number_from_string(string: str) -> int:
    number = re.sub("[^\d]", "", string)
    number_int = int(number)
    if number_int >= 0:
        return number_int
    else:
        raise Exception(f"Got weird number of entries on page: ({number_int})")
