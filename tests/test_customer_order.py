from unittest import TestCase

from customer_order import CustomerOrder


class CustomerOrderBase(TestCase):
    line_order = None
    customer_order = None
    orders = None

    sample_data = {"order_type": "milk",
                   "cash": 12,
                   "price": 3,
                   "bonus_ratio": 2,
                   }

    def configure_data(self):
        for key, value in self.sample_data.items():
            setattr(self.customer_order, key, value)

    def setUp(self):
        self.customer_order = CustomerOrder()
        self.configure_data()

    def test_input(self):
        for key, value in self.sample_data.items():
            self.assertEqual(getattr(self.customer_order, key), value)

    def test_calculate_initial_buy(self):
        expected = self.sample_data["cash"] / self.sample_data["price"]
        self.assertEqual(self.customer_order.calculate_initial_buy(), expected)

    def test_calculate_bonus_pack(self):
        initial_buy = self.sample_data["cash"] / self.sample_data["price"]
        expected = initial_buy / self.sample_data["bonus_ratio"]
        self.assertEqual(
            self.customer_order.calculate_bonus_pack(), expected)
