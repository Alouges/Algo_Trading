from abc import ABCMeta, abstractmethod


class AbstractData(object, metaclass=ABCMeta):
    """
        Abstract class which will help to ensure other 'Data' class respect this template.
    """

    #################################################
    #                  PROPERTIES                   #
    #################################################
    @property
    @abstractmethod
    def for_ccy(self):
        """
            Returns the foreign ccy of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @for_ccy.setter
    @abstractmethod
    def for_ccy(self, val):
        """
            Sets the foreign ccy of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def dom_ccy(self):
        """
            Returns the domestic ccy of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @dom_ccy.setter
    @abstractmethod
    def dom_ccy(self, val):
        """
            Sets the domestic ccy of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def ccy_pair(self):
        """
            Returns the ccy pair of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @ccy_pair.setter
    @abstractmethod
    def ccy_pair(self, val):
        """
            Sets the ccy pair of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def name(self):
        """
            Returns the full name of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @name.setter
    @abstractmethod
    def name(self, val):
        """
            Sets the full name of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def granularity(self):
        """
            Returns the granularity of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @granularity.setter
    @abstractmethod
    def granularity(self, val):
        """
            Sets the granularity of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def timestamps(self):
        """
            Returns the timestamps of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @timestamps.setter
    @abstractmethod
    def timestamps(self, val):
        """
            Sets the timestamps of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def bids(self):
        """
            Returns the bids of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @bids.setter
    @abstractmethod
    def bids(self, val):
        """
            Sets the bids of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @property
    @abstractmethod
    def asks(self):
        """
            Returns the asks of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    @asks.setter
    @abstractmethod
    def asks(self, val):
        """
            Sets the asks of the asset.
        """
        raise NotImplementedError("Abstract method executed.")

    #################################################
    #                   METHODS                     #
    #################################################
    @abstractmethod
    def load_data(self, from_timestamp, to_timestamp):
        """
            Loads the data between indicated timestamps.
        """
        raise NotImplementedError("Abstract method executed.")

    @abstractmethod
    def get_bid(self, timestamp):
        """
            Returns the nearest bid of the corresponding timestamp.
        """
        raise NotImplementedError("Abstract method executed.")

    @abstractmethod
    def get_live_bid(self):
        """
            Returns the last bid.
        """
        raise NotImplementedError("Abstract method executed.")

    @abstractmethod
    def get_ask(self, timestamp):
        """
            Returns the nearest ask of the corresponding timestamp.
        """
        raise NotImplementedError("Abstract method executed.")

    @abstractmethod
    def get_live_ask(self):
        """
            Returns the last ask.
        """
        raise NotImplementedError("Abstract method executed.")
