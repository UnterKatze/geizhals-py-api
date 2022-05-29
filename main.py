import requests
from enums import BaseURL, CathegoryKeywords, SortingOptions, NvidiaGPUs
from helper_fn import *

# search strings
CAT_STR = "?cat="
SORTING_STR = "&sort="
PRODUCT_STR = "&xf="


class GeizhalsPyAPI:
    def __init__(self, baseURL: str = BaseURL.DE_DOMAIN.value):
        self.url = None
        self.cat = None
        self.sorting = None
        self.product = None
        self.baseURL = baseURL
        self.html_cont = None
        self.entries = {}
        self.entries_on_page = None

    def get_html_content(self):
        if self.product is None:
            self.url = (
                self.baseURL + CAT_STR + self.cat.value + SORTING_STR + self.sorting
            )
        else:
            self.url = (
                self.baseURL
                + CAT_STR
                + self.cat.value
                + SORTING_STR
                + self.sorting
                + PRODUCT_STR
                + self.product.value
            )
        resp = requests.get(self.url)
        if resp.status_code == 200:
            self.html_cont = resp.text
        else:
            raise Exception(f"Error {resp.status_code}. {resp.reason}.")

    def get_number_of_entries_on_page(self):
        html_cont_copy = self.html_cont
        if "category_list__empty-list" in html_cont_copy:
            self.entries_on_page = 0
            return
        entry_number_on_page_str = (
            html_cont_copy.split('<div class="productlist__item productlist__name">')[
                -1
            ]
            .split('rel="nofollow">\n')[1]
            .split("\n")[0]
        )
        self.entries_on_page = get_number_from_string(entry_number_on_page_str)
        return

    def get_entries(
        self,
        cat: CathegoryKeywords,
        product: NvidiaGPUs = None,
        sorting: str = SortingOptions.POPULARITY.value,
        nr_of_entries: int = 10,
    ):
        self.cat = cat
        self.sorting = sorting
        self.product = product
        self.get_html_content()
        self.get_number_of_entries_on_page()
        # if number of entries on page is smaller than requested number of entries
        if nr_of_entries < 1 or nr_of_entries > 30:
            raise Exception("Number of entries to get must be between 1 and 30.")
        if self.entries_on_page < nr_of_entries:
            nr_of_entries = self.entries_on_page
        if nr_of_entries <= 0:
            raise Exception(f"The product {self.product.name} is not available.")
        if self.product is not None and self.product.name not in self.html_cont:
            self.entries[
                0
            ] = f"The product {product.name} was not found in cathegorie {self.cat.name}."
            return self.entries
        for i in range(nr_of_entries):
            entry_str = self.html_cont.split(f'id="product{i}"')[-1].split(
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
                "nr": i + 1,
                "name": entry_name,
                "price": entry_price_numeric,
                "currency": currency,
            }
            self.entries[i] = entry
        return self.entries


if __name__ == "__main__":
    ghAPI = GeizhalsPyAPI(baseURL=BaseURL.DE_DOMAIN.value)
    entries_dict = ghAPI.get_entries(
        cat=CathegoryKeywords.GPU_PCIE,
        product=NvidiaGPUs.RTX2070S,
        sorting=SortingOptions.PRICE_LOWEST.value,
        nr_of_entries=10,
    )
    for key in entries_dict:
        print(entries_dict[key])
