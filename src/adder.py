from operator import add


class Adder:
    otype = None
    number = None
    _out = None
    result = None

    def __init__(self, otype, number):
        self.otype = otype
        self.number = number
        self.__cal_out()

    def __cal_out(self):
        n = {'milk': [1, 0, 0],
             'dark': [0, 1, 0],
             'white': [0, 0, 1]}
        self._out = [i * self.number for i in n[self.otype]]

    def adder(self, list_line):
        self.result = list(map(add, self._out, list_line))
        return self.result

    @property
    def out(self):
        return self._out
