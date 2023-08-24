# class Order:
#     def __init__(self) -> None:
#         pass
    
# class OrderBook:
#     def __init__(self) -> None:
#         pass

# class Position:
#     def __init__(self) -> None:
#         pass
import json

class Kline:
    """Kline object.

    Args:
        platform: Exchange platform name, e.g. `binance` / `bitmex`.
        symbol: Trade pair name, e.g. `ETH/BTC`.
        open: Open price.
        high: Highest price.
        low: Lowest price.
        close: Close price.
        volume: Total trade volume.
        timestamp: Update time, millisecond.
        kline_type: Kline type name, `kline`, `kline_5min`, `kline_15min` ... and so on.
    """

    # def __init__(self, symbol=None, open=None, high=None, low=None, close=None, volume=None,
    #              timestamp=None, kline_type=None):
        # self.symbol = symbol
        # self.open = open
        # self.high = high
        # self.low = low
        # self.close = close
        # self.volume = volume
        # self.timestamp = timestamp
        # self.kline_type = kline_type
        
    def __init__(self) -> None:
        pass
        

    @property
    def data(self):
        d = {
            "start_time": self.start_time,
            "close_time": self.close_time,
            "symbol": self.symbol,
            "interval": self.interval,
            "first_trade_id": self.first_trade_id,
            "last_trade_id": self.last_trade_id,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "base_asset_volume": self.base_asset_volume,
            "trade_num": self.trade_num,
            "is_closed": self.is_closed,
            "quote_asset_volume": self.quote_asset_volume,
            "taker_buy_base_asset_volume": self.taker_buy_base_asset_volume,
            "taker_buy_quote_asset_volume": self.taker_buy_quote_asset_volume,
        }
        return d

    @property
    def smart(self):
        d = {            
            "t": self.start_time,
            "T": self.close_time,
            "s": self.symbol,
            "i": self.interval,
            "f": self.first_trade_id,
            "L": self.last_trade_id, 
            "o": self.open,
            "c": self.close,
            "h": self.high,
            "l": self.low,
            "v": self.base_asset_volume,
            "n": self.trade_num,
            "x": self.is_closed,
            "q": self.quote_asset_volume,
            "V": self.taker_buy_base_asset_volume,
            "Q": self.taker_buy_quote_asset_volume
        }
        return d

    def load_smart(self, d):
        self.start_time = d["t"]
        self.close_time = d["T"]
        self.symbol = d["s"]
        self.interval = d["i"]
        self.first_trade_id = d["f"]
        self.last_trade_id = d["L"]
        self.open = d["o"]
        self.close = d["c"]
        self.high = d["h"]
        self.low = d["l"]
        self.base_asset_volume = d["v"]
        self.trade_num = d["n"]
        self.is_closed = d["x"]
        self.quote_asset_volume = d["q"]
        self.taker_buy_base_asset_volume = d["V"]
        self.taker_buy_quote_asset_volume = d["Q"]
        
        return self

    def __str__(self):
        info = json.dumps(self.data)
        return info

    def __repr__(self):
        return str(self)


class Market:
    """Subscribe Market.

    Args:
        market_type: Market data type,
            MARKET_TYPE_TRADE = "trade"
            MARKET_TYPE_ORDERBOOK = "orderbook"
            MARKET_TYPE_KLINE = "kline"
            MARKET_TYPE_KLINE_5M = "kline_5m"
            MARKET_TYPE_KLINE_15M = "kline_15m"
        platform: Exchange platform name, e.g. `binance` / `bitmex`.
        symbol: Trade pair name, e.g. `ETH/BTC`.
        callback: Asynchronous callback function for market data update.
                e.g. async def on_event_kline_update(kline: Kline):
                        pass
    """

    def __init__(self, market_type, platform, symbol, callback):
        """Initialize."""
        if platform == "#" or symbol == "#":
            multi = True
        else:
            multi = False
        if market_type == const.MARKET_TYPE_ORDERBOOK:
            from aioquant.event import EventOrderbook
            EventOrderbook(Orderbook(platform, symbol)).subscribe(callback, multi)
        elif market_type == const.MARKET_TYPE_TRADE:
            from aioquant.event import EventTrade
            EventTrade(Trade(platform, symbol)).subscribe(callback, multi)
        elif market_type in [
            const.MARKET_TYPE_KLINE, const.MARKET_TYPE_KLINE_3M, const.MARKET_TYPE_KLINE_5M,
            const.MARKET_TYPE_KLINE_15M, const.MARKET_TYPE_KLINE_30M, const.MARKET_TYPE_KLINE_1H,
            const.MARKET_TYPE_KLINE_3H, const.MARKET_TYPE_KLINE_6H, const.MARKET_TYPE_KLINE_12H,
            const.MARKET_TYPE_KLINE_1D, const.MARKET_TYPE_KLINE_3D, const.MARKET_TYPE_KLINE_1W,
            const.MARKET_TYPE_KLINE_15D, const.MARKET_TYPE_KLINE_1MON, const.MARKET_TYPE_KLINE_1Y]:
            from aioquant.event import EventKline
            EventKline(Kline(platform, symbol, kline_type=market_type)).subscribe(callback, multi)
        else:
            logger.error("market_type error:", market_type, caller=self)

    
    
    
    
class KlineBook:
    def __init__(self) -> None:
        EventKline(Kline(platform, symbol, kline_type=market_type)).subscribe(callback, multi)
        pass
