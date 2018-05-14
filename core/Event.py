import datetime

class Event:
    """
        Event class
    """

    type = None
    date = None

    def print_info(self):
        print(self.date)
        print(self.type)


class MarketEvent(Event):

    def __init__(self):
        self.type = 'MARKET'
        self.date = datetime.datetime.now()


class SignalEvent(Event):

    symbol = None
    signal_type = None

    def __init__(self, time_stamp, symbol, signal_type):
        self.type = 'SIGNAL'
        self.date = time_stamp
        self.symbol = symbol
        self.signal_type = signal_type


class OrderEvent(Event):

    signal_type = None
    symbol = None
    order_type = None
    direction = None

    def __init__(self, symbol, order_type, quantity, direction):
        self.type = 'ORDER'
        self.symbol = symbol
        self.order_type = order_type
        self.quantity = quantity
        self.direction = direction

    def print_order(self):
        print("Order: Symbol=%s, Type=%s, Quantity=%s, Direction=%s" %\
            (self.symbol, self.order_type, self.quantity, self.direction))


class FillEvent(Event):

    def __init__(self, time_stamp, symbol, exchange, quantity, direction, fill_cost, commission=None):
        self.type = 'FILL'
        self.date = time_stamp
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost

        # Calculate commission
        if commission is None:
            self.commission = self.calculate_kraken_commission()
        else:
            self.commission = commission
    
    def calculate_kraken_commission(self):
            full_cost = 0.016 * self.quantity
            return full_cost
