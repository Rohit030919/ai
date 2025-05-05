class StockMarketTrading:
    def __init__(self):
        self.stocks = {
            'AAPL': 150,
            'GOOG': 2800,
            'AMZN': 3400,
            'TSLA': 700
        }

    def buy_stock(self, stock, amount):
        if stock in self.stocks:
            return f"Buying {amount} of {stock} at ${self.stocks[stock]} per stock."
        else:
            return "Stock not available."

    def sell_stock(self, stock, amount):
        if stock in self.stocks:
            return f"Selling {amount} of {stock} at ${self.stocks[stock]} per stock."
        else:
            return "Stock not available."

stock_system = StockMarketTrading()
print(stock_system.buy_stock('AAPL', 10))
print(stock_system.sell_stock('GOOG', 5))
print(stock_system.buy_stock('MSFT', 2))
