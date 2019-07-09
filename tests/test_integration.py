from unittest import TestCase

from process_orders import Pipeline
from operator import add
from adder import Adder


class IntegrationBase(TestCase):
    pipeline = None
    line_item = None

    expected = ['milk 7,dark 0,white 0', 'milk 0,dark 9,white 0',
                'milk 1,dark 0,white 4']

    def setUp(self) -> None:
        self.pipeline = Pipeline("./fixtures/testorders.csv")
        self.pipeline.run_pipeline()
        self.line_item = self.pipeline.line_item
        print(self.line_item)

    def test_integration(self):
        self.assertEqual(self.line_item, self.expected)
        print("\n\nLine_item:(i/o):")
        for i in self.line_item:
            print(i)
