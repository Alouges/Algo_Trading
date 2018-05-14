import datetime

from abc import ABCMeta, abstractmethod

from core.Event import FillEvent, OrderEvent
"""
Improvement : add sliperage + not mid execution + failed execution
"""
class ExecutionHandler(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute_order(self, event):
        raise NotImplementedError("Should implement execute_order()")


class SimulatedExecutionHandler(ExecutionHandler):

    def __init__(self, events):
        self.events = events

    def execute_order(self, event):

        if event.type == 'ORDER':
            fill_event = FillEvent(datetime.datetime.utcnow(), event.symbol,
                                   'KRAKEN', event.quantity, event.direction, None)
            self.events.put(fill_event)