from engine.market import KlineBook
from engine.market import Kline

class MA:
    def __init__(self, length=10, type=None) -> None:
        klines = []
        self.length = length
        self.type = type
        self.on_kline_update = self._on_kline_update
        # register self to market
        
        
    def _on_kline_update(self, kline: Kline):
        if len(self.klines) > self.length:
            self.klines.pop(0)
        self.klines.append(kline)
        
    def get(self):
        pass