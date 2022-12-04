##### Imports #####

from calendar import c
from datetime import datetime, timedelta
from logging import raiseExceptions
import requests

##### Class #####


class Coin:
    """
    Class for create crypto coins object

    Default use:
    * Create object coin
    * Get historical values from coins
    * Get currently info from coins

    API:
        Used mercadobitcoin API.
        Mercado Bitcoin is the biggest platform of cryptocurrency
        from LATAM.
        The API documentation can be accessed by the following link:
        https://www.mercadobitcoin.com.br/api-doc/


    Attributes
    ----------
    code : str
        Code crypto coin from API.
        The list of codes and the respectives names can be accessed in API documentation.

    name : str
        Crypto coin name.

    Methods
    -------
    get_currently_info(method:str)
        Get all coin information from API in current day

    get_info_by_date(date:datetime = datetime.now()- timedelta(days = 1))
        Get all coin information on a defined date

    get_all_history_info()
        Get all coin information from scratch date until d-1

    """

    def __init__(self, code: str, name: str) -> None:
        self.code = code
        self.name = name
        self.__url_api = f"https://www.mercadobitcoin.net/api/{code}/"

    def __get_d_minus_1() -> datetime:
        return datetime.now() - timedelta(days=1)

    def get_current_info(self, method: str = "ticker") -> dict:
        """
        Class Method that get current info from API.

        Parameters
        ----------
        method : str
            Consult method from API.Values accepted:
                - ticker : Summary of executed transactions
                - orderbook : Trade book, open buy and sell orders
                - trades : History of operations performed
            default method: ticker
        return: json
            return json with crypto informations from current day

        """
        try:
            url_consult = self.__url_api + method
            request = requests.get(url_consult)
            if request.ok:
                print("Connection Success!\n")
                return requests.get(url_consult).json()
            print("Connection with API Failed!")

        except Exception as error:
            print("Json Conversion Failed!\n", error)
            pass

    def get_info_by_date(self, date: datetime = __get_d_minus_1()) -> dict:
        """
        Class Method that get coin info from API in passed date.

        Parameters
        ----------
        date : datetime
            Date to consult coin information
        return: json
            return json with crypto informations from passed parameters date
        """
        try:
            url_consult = (
                self.__url_api + f"day-summary/{date.year}/{date.month}/{date.day}"
            )
            request = requests.get(url_consult)
            if request.ok:
                print("Connection Success!\n")
                return requests.get(url_consult).json()
            print("Connection with API Failed!")
        except Exception as error:
            print("Json Conversion Failed!\n", error)
            pass

    def get_all_history_info(self) -> list:
        """
        Class Method that get coin info from API in passed date.

        Parameters
        ----------
        None

        return: list
            return a list of json with all dates crypto information
        """
        try:
            list = []
            date_init = datetime.now() - timedelta(days=1)
            while True:
                try:

                    list.append(self.get_info_by_date(date_init))
                    print(date_init)
                    date_init = date_init - timedelta(days=1)
                except:
                    print("Done")
                    return list
        except Exception as error:
            print("Error! Something went wrong when getting history info.\n", error)


if __name__ == "__main__":
    bitcoin = Coin("btc", "Bitcoin")
    bitcoin.get_current_info()
