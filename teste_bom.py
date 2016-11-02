import unittest
import list_sum


class List_sumTest(unittest.TestCase):
    def test_list_sum(self):
        assert list_sum.soma_lista(list_sum.numbers) == 9
