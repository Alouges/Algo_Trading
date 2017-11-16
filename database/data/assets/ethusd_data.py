from database.data.abstract_data import AbstractData
from database.data.constants import Constants


class BTCUSDData(AbstractData):
    """
        Concrete implementation of AbstractData for the ETH vs USD ccy pair.
    """

    #################################################
    #                  VARIABLES                    #
    #################################################
    __for_ccy = None
    __dom_ccy = None
    __ccy_pair = None
    __name = None
    __granularity = None
    __timestamps = None
    __bids = None
    __asks = None

    #################################################
    #                 CONSTRUCTOR                   #
    #################################################
    def __init__(self):
        """
            Initialize attributes as ETH vs USD asset
        """
        self.__for_ccy = Constants.ETHEREUM_CODE
        self.__dom_ccy = Constants.DOLLAR_CODE
        self.__ccy_pair = self.__for_ccy + "/" + self.__dom_ccy
        self.__name = Constants.ETHEREUM_NAME + "/" + Constants.DOLLAR_NAME
        self.__granularity = None
        self.__timestamps = None
        self.__bids = None
        self.__asks = None

    #################################################
    #                  PROPERTIES                   #
    #################################################
    @property
    def for_ccy(self):
        """
            Returns the foreign ccy of the asset.
        """
        return self.__for_ccy

    @for_ccy.setter
    def for_ccy(self, val):
        """
            Sets the foreign ccy of the asset.
        """
        self.__for_ccy = val

    @property
    def dom_ccy(self):
        """
            Returns the domestic ccy of the asset.
        """
        return self.__dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, val):
        """
            Sets the domestic ccy of the asset.
        """
        self.__dom_ccy = val

    @property
    def ccy_pair(self):
        """
            Returns the ccy pair of the asset.
        """
        return self.__ccy_pair

    @ccy_pair.setter
    def ccy_pair(self, val):
        """
            Sets the ccy pair of the asset.
        """
        self.__ccy_pair = val

    @property
    def name(self):
        """
            Returns the full name of the asset.
        """
        return self.__name

    @name.setter
    def name(self, val):
        """
            Sets the full name of the asset.
        """
        self.__name = val

    @property
    def granularity(self):
        """
            Returns the granularity of the asset.
        """
        return self.__granularity

    @granularity.setter
    def granularity(self, val):
        """
            Sets the granularity of the asset.
        """
        self.__granularity = val

    @property
    def timestamps(self):
        """
            Returns the timestamps of the asset.
        """
        return self.__timestamps

    @timestamps.setter
    def timestamps(self, val):
        """
            Sets the timestamps of the asset.
        """
        self.__timestamps = val

    @property
    def bids(self):
        """
            Returns the bids of the asset.
        """
        return self.__bids

    @bids.setter
    def bids(self, val):
        """
            Sets the bids of the asset.
        """
        self.__bids = val

    @property
    def asks(self):
        """
            Returns the asks of the asset.
        """
        return self.__asks

    @asks.setter
    def asks(self, val):
        """
            Sets the asks of the asset.
        """
        self.__asks = val

    #################################################
    #                   METHODS                     #
    #################################################
    def load_data(self, from_timestamp, to_timestamp):
        """
            Loads the data between indicated timestamps.
        """
        raise NotImplementedError()

    def get_bid(self, timestamp):
        """
            Returns the nearest bid of the corresponding timestamp.
        """
        raise NotImplementedError()

    def get_live_bid(self):
        """
            Returns the last bid.
        """
        raise NotImplementedError()

    def get_ask(self, timestamp):
        """
            Returns the nearest ask of the corresponding timestamp.
        """
        raise NotImplementedError()

    def get_live_ask(self):
        """
            Returns the last ask.
        """
        raise NotImplementedError()
