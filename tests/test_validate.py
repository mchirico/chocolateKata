from unittest.mock import patch
from unittest import TestCase

from utils.validate import ValidateInput


class ValidateInputBase(TestCase):
    line_order = None
    customer_order = None
    orders = None
    test_and_expected = [
        (["white", '15', '2', '3'], True),
        (['"milk"', '15', '2', '3'], True),
        (['"dark"', '15', '2', '3'], True),
        (['white', '15', '2', '3'], True),
        (['milk', '15', '2', '3'], True),
        (['dark', '15', '2', '3'], True),
        (['milk', '15', '2', '3'], True),
        (['bad', '15', '2', '3'], False),
        (['milk', 3, '3', '1'], False),
        (['milk', 'donut', '3', '1'], False),
        ([3, '8', '3', '1'], False),
        (['white', '8', '3', '1', '9'], False),
        (['8', 'white', '1', '9'], False),
    ]

    def setUp(self):
        self.line_order = ValidateInput()

    def test_quote_strip(self):
        self.line_order.set(['"milk', '1', '1', '1'])
        result = self.line_order.value[0]
        self.assertEqual('milk', result)

    def test_input(self):
        for (input, expected) in self.test_and_expected:
            assert self.line_order.set(input) is expected
