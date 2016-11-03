class Portfolio(object):
    """A simple stock portfolio"""

    def __init__(self):
        # stocks is a list of lists:
        #   [[name, shares, price], ...]
        self.stocks = []

    def buy(self, name, shares, price):
        """Buy `name`: `shares` shares at `price`."""
        self.stocks.append([name, shares, price])

    def cost(self):
        """What was the total cost of this portfolio?"""
        amt = 0.0
        for name, shares, price in self.stocks:
            amt += shares * price
        return "USD%d" % amt

    def sell(self, name, shares):
        """Sell some shares."""
        for holding in self.stocks:
            if holding[0] == name:
                if holding[1] < shares:
                    raise ValueError("Not enough shares")
                holding[1] -= shares
                break
        else:
            raise ValueError("You don't own that stock")

    def sum_prices(self):
        prices = []
        for stock in self.stocks:
            prices.append(stock[1] * stock[2])
        return sum(prices)

        # p = Portfolio()
        # p.buy("IBM", 100, 120.10)
        # p.buy("ADP", 200, 90.00)
        # print(p.stocks)
        # print(p.cost())
