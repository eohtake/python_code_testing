import unittest
from portfolio1 import Portfolio


class PortfolioTestCase(unittest.TestCase):
    """Base class for all Portfolio tests."""

    def assertCostEqual(self, p, cost):
        """Assert that `p`'s cost is equal to `cost`.
        Este metodo recebe dois parametros:
        1: A instancia(obj) criada de Portfolio(). p = Portfolio()
        2: O valor contra o qual sera feito o teste de igualdade.
        Interessante notar que o metodo assertEqual 'e utilizado passando-se dois argumentos:
        1: O metodo Portfolio.cost() que faz o calculo e retorna o valor total de todas as acoes possuidas.
        2: O valor total esperado que sera comparado com o valor retornado do metodo Porfolio.cost()
        Veja que nos metodos de testes, o metodo p.cost() nunca e passado, e sim apenas a instancia de
        Portfolio() que 'e representada pela variavel 'p'. Com este objeto disponivel aqui, 'e possivel
        utilizar o metodo cost() que veio junto com o objeto p de Portfolio(), ou qualquer outro metodo"""

        self.assertEqual(p.cost(), cost)


class PortfolioTest(PortfolioTestCase):
    def setUp(self):
        self.p = Portfolio()

    def test_total_cost_for_empty_portfolio_must_return_zero(self):
        self.assertCostEqual(self.p, "USD%d" % 0.0)


class PortfolioBuyTest(PortfolioTest):
    def test_buy_one_stock_must_return_portfolio_total_cost(self):
        self.p.buy("IBM", 100, 176.48)
        self.assertCostEqual(self.p, "USD%d" % 17648) # Utilizando este metodo, o teste mostra a diferenca qdo o teste da errado.

    def test_buy_two_stocks_must_return_portfolio_total_cost(self):
        self.p.buy("IBM", 100, 176.47)
        self.p.buy("HPQ", 100, 36.15)
        self.assertEqual(self.p.cost(), "USD%d" % 21262.0)

    def test_bad_input_while_buying_a_stock_without_quantity_and_price_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.p.buy("IBM")

    def test_bad_input_while_buying_a_stock_without_price_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.p.buy("IBM", 100)

    def test_bad_input_while_buying_a_stock_without_quantity_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.p.buy("IBM", 0, 123.05)

    def test_bad_input_while_buying_a_stock_without_name_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.p.buy("", 100, 123.05)

    def test_bad_input_nothing_was_informed_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.p.buy()

class PortfolioSellTest(PortfolioTestCase):
    # Invoked before each test method
    # O metodo setUp deve conter as configuracoes necessarias para rodar os testes seguintes.
    # No exemplo abaixo por exemplo, nao e preciso criar uma instancia de Portfolio() em todos os
    # metodos de testes, basta criar em setUp() e depois acessar apenas o self.p.
    # Da mesma forma, todas as acoes sao compradas no setUp, assim nao precisa repetir nos testes.

    def setUp(self):
        self.p = Portfolio()
        self.p.buy("MSFT", 100, 27.0)
        self.p.buy("DELL", 100, 17.0)
        self.p.buy("ORCL", 100, 34.0)

    def test_sell_stock_should_decrease_portfolio_and_return_new_total(self):
        self.p.sell("MSFT", 50)
        self.assertCostEqual(self.p, "USD%d" % 6450)

    def test_sell_stocks_which_qty_dont_own_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.p.sell("MSFT", 200)

    def test_sell_dont_owned_stocks_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.p.sell("IBM", 1)

















