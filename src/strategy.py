class Strategy:
    order_base = None
    _strategy = {'white': {'white': 1, 'milk': 1, 'dark': 0},
                 'milk': {'white': 0, 'milk': 1, 'dark': 0},
                 'dark': {'white': 0, 'milk': 0, 'dark': 2}}

    _order_type = None

    def __init__(self,
                 strategy=None):
        if strategy is not None:
            self._strategy = strategy

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order):
        self._order_type = order

    def calculate_bonus_on(self, o_type):
        if self._order_type in self._strategy:
            return self._strategy[self.order_type].get(o_type, 0)
