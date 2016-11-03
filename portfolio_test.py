import unittest
from portfolio1 import Portfolio

class PortfolioTestCase(unittest.TestCase):
    """Base class for all Portfolio tests."""

    def assertCostEqual(self, p, cost):
        """Assert that `p`'s cost is equal to `cost`."""
        self.assertEqual(p.cost(), cost)

class PortfolioTest(PortfolioTestCase):
    def test_empty(self):
        p = Portfolio()
        assert p.cost() == "USD%d" % p.sum_prices()  # Sem utilizacao da base class

    def test_buy_one_stock(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        self.assertCostEqual(p, "USD%d" % p.sum_prices()) # Utilizando este metodo, o teste mostra a diferenca qdo o teste da errado.

    def test_buy_two_stocks(self):
        p = Portfolio()
        p.buy("IBM", 100, 176.48)
        p.buy("HPQ", 100, 36.15)
        self.assertEqual(p.cost(), "USD%d" % 21263.0) # Sem utilizacao da base class

    def test_bad_input(self):
        p = Portfolio()
        with self.assertRaises(TypeError):
            p.buy("IBM")

    def test_total_sum(self):
        p = Portfolio()
        p.buy("IBM", 103, 176.48)
        self.assertEqual(p.sum_prices(), 18177.44)

class PortfolioSellTest(PortfolioTestCase):
    # Invoked before each test method
    def setUp(self):
        self.p = Portfolio()
        self.p.buy("MSFT", 100, 27.0)
        self.p.buy("DELL", 100, 17.0)
        self.p.buy("ORCL", 100, 34.0)

    def test_sell(self):
        self.p.sell("MSFT", 50)
        self.assertCostEqual(self.p, "USD%d" % 6450)

    def test_not_enough(self):
        with self.assertRaises(ValueError):
            self.p.sell("MSFT", 200)

    def test_dont_own_it(self):
        with self.assertRaises(ValueError):
            self.p.sell("IBM", 1)

















