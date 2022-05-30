from gh_py_api import GeizhalsPyAPI
from helper_enums import BaseURL, CategoryKeywords, NvidiaGPUs, SortingOptions
import time

# set domain
DOMAIN = BaseURL.DE_DOMAIN.value
# set category
CAT = CategoryKeywords.GPU_PCIE
# set lineup to compare
LINEUP = NvidiaGPUs

if __name__ == "__main__":
    ghAPI = GeizhalsPyAPI(baseURL=DOMAIN)
    for prod in LINEUP:
        # get 5 cheapest items of each product in the lineup TODO there is a bug
        entries_dict = ghAPI.get_entries(
            cat=CAT,
            product=prod,
            sorting=SortingOptions.PRICE_LOWEST.value,
            nr_of_entries=5,
        )
        # sleep for 1s to avoid ban from gh
        time.sleep(1)
        if len(entries_dict) > 1:
            for key in entries_dict:
                print(entries_dict[key])

            # get average price of 5 cheapest products
            price_sum = 0
            num_dicts = 0
            for key in entries_dict:
                price_sum += entries_dict[key]["price"]
                num_dicts += 1
            avg_price = price_sum / num_dicts
            print(f"Average Price of Product: {round(avg_price)} €")
