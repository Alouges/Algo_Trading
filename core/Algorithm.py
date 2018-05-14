import datetime
import numpy as np
import pandas as pd
import queue

from abc import ABCMeta, abstractmethod

from core.Event import SignalEvent


class Algorithm(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def compute_signals(self):
        raise NotImplementedError("Should implement compute_signals()")


class BuyAndHoldAlgorithm(Algorithm):
    def __init__(self, bars, events):
        self.bars = bars
        self.symbol_list = self.bars.symbol_list
        self.events = events

        # Once buy & hold signal is given, these are set to True
        self.bought = self._compute_initial_bought()

    def _compute_initial_bought(self):
        bought = {}
        for s in self.symbol_list:
            bought[s] = False
        return bought

    def compute_signals(self, event):
        if event.type == 'MARKET':
            for s in self.symbol_list:
                bars = self.bars.get_latest_bars(s, N=1)
                if bars is not None and bars != []:
                    if not self.bought[s]:
                        # (Symbol, Datetime, Type = LONG, SHORT or EXIT)
                        signal = SignalEvent(bars[0][1], bars[0][0], 'LONG')
                        self.events.put(signal)
                        self.bought[s] = True

