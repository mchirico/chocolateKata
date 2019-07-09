from unittest.mock import patch
from unittest import TestCase

from utils.reader import Reader


class ReaderBase(TestCase):
    result = None
    reader = None

    read_fixture = [
        'type, cash, price, bonus_ratio',
        '"white",15, 2, 3',
        '"milk", 12, 2, 5',
        '"dark", 13, 4, 1',
        '"white", 6, 2, 2',
        '"bozo", 3, 2, 1',
    ]

    expected_result = [['"white"', '15', ' 2', ' 3'],
                       ['"milk"', ' 12', ' 2', ' 5'],
                       ['"dark"', ' 13', ' 4', ' 1'],
                       ['"white"', ' 6', ' 2', ' 2'],
                       ['"bozo"', ' 3', ' 2', ' 1']]

    def setUp(self):
        self.reader = Reader("")

    @patch("utils.reader.Reader.read")
    def test_read_and_split(self, read):
        read.return_value = self.read_fixture
        self.assertEqual(self.reader.result(), self.expected_result)

    @patch("utils.reader.Reader.read")
    def test_split(self, read):
        read.return_value = ['Skip heading..\n', 'valid,data\n']

        expected = [['valid', 'data']]
        self.assertEqual(self.reader.split(), expected)
