#!/usr/bin/env python3
"""


"""

from utils.reader import Reader
from utils.validate import ValidateInput
from customer_order import CustomerOrder

ORDERS = '../input/orders.csv'


class Pipeline:
    _file = None
    _line_item = None

    def __init__(self, file=ORDERS):
        self._file = file

    @property
    def line_item(self):
        return self._line_item

    def print_items(self):
        for i in self.line_item:
            print(i)

    def run_pipeline(self):
        customer_order = CustomerOrder()

        read = Reader(self._file)
        line_order = ValidateInput()

        self._line_item = []

        for order in read.result():
            line_order.set(order)
            if line_order.valid_types:
                customer_order.order_type = line_order.value[0]
                customer_order.cash = line_order.value[1]
                customer_order.price = line_order.value[2]
                customer_order.bonus_ratio = line_order.value[3]
                self._line_item.append(customer_order.final_order)


if __name__ == '__main__':
    p = Pipeline(ORDERS)
    p.run_pipeline()
    p.print_items()
