from strategy import Strategy
from adder import Adder


class CustomerOrder:
    _order_type = None
    _cash = None
    _price = None
    _bonus_ratio = None
    bonus_pack = None

    _strategy = None
    _adder_final_no_text = None

    def __init__(self, strategy=Strategy()):
        self._strategy = strategy

    @property
    def final_order(self):
        self._strategy.order_type = self._order_type
        bp = self.calculate_bonus_pack()
        milk = bp * self._strategy.calculate_bonus_on('milk')
        dark = bp * self._strategy.calculate_bonus_on('dark')
        white = bp * self._strategy.calculate_bonus_on('white')
        bonus = [milk, dark, white]
        initial_purchase = self.calculate_initial_buy()
        adder = Adder(self._order_type, initial_purchase)
        self._adder_final_no_text = adder.adder(bonus)
        r = adder.adder(bonus)
        return 'milk {},dark {},white {}'.format(r[0], r[1], r[2])

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        self._order_type = order_type

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, cash):
        self._cash = cash

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def bonus_ratio(self):
        return self._bonus_ratio

    @bonus_ratio.setter
    def bonus_ratio(self, bonus_ratio):
        self._bonus_ratio = bonus_ratio

    def calculate_initial_buy(self):
        return int(self._cash / self._price)

    def calculate_bonus_pack(self):
        return int(self.calculate_initial_buy() / self._bonus_ratio)
