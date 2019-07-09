
from unittest import TestCase

from strategy import Strategy


class StrategyUnitTest(TestCase):
    line_order = None
    customer_order = None

    expected_result = {'white': {'white': 1, 'milk': 1, 'dark': 0},
                       'milk': {'white': 0, 'milk': 1, 'dark': 0},
                       'dark': {'white': 0, 'milk': 0, 'dark': 2}}

    def test_strategy(self):
        strategy = Strategy()
        for key in self.expected_result:
            strategy.order_type = key
            self.assertEqual(
                strategy.calculate_bonus_on('white'),
                self.expected_result[key]['white'])
            self.assertEqual(
                strategy.calculate_bonus_on('milk'),
                self.expected_result[key]['milk'])
            self.assertEqual(
                strategy.calculate_bonus_on('dark'),
                self.expected_result[key]['dark'])
