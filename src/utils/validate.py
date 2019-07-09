#!/usr/bin/env python3


def convert_to_int(val):
    return [int(i) for i in val]


def strip_quotes(val):
    return [i.replace('"', '').replace("'", "") for i in val if
            isinstance(i, str)]


class ValidateInput:
    _line_item = None
    _values = None
    _history_input = []

    _validate = {'first': ["white", "dark", "milk",
                           '"white"', '"dark"', '"milk"'],
                 'expected_initial': [type(i) for i in
                                      ['string', 'string', 'string',
                                       'string']],
                 'expected': [type(i) for i in ['string', 0, 0, 0]],
                 'convert_function': convert_to_int,
                 'preprocess_function': strip_quotes,
                 'length': 4}

    def __init__(self,
                 validate=None):
        if validate is not None:
            self._validate = validate

    def preprocess_function(self, input):
        return self._validate['preprocess_function'](input)

    def set(self, values):
        values = self.preprocess_function(values)
        self._values = values
        return self._status()

    def _status(self):
        status_check = self.valid_first and self.valid_types
        self._history_input.append(status_check)
        return status_check

    @property
    def log(self):
        bad_entries = self._history_input.count(False)
        good_entries = self._history_input.count(True)
        return bad_entries, good_entries

    @property
    def value(self):
        return self._values

    @property
    def valid_length(self):
        return self._validate['length'] == len(self._values)

    @property
    def valid_types(self):
        tv = [type(i) for i in self._values]
        if tv == self._validate['expected_initial']:
            try:
                self.convert_types(1)
            except ValueError:
                return False

        return [type(i) for i in self._values] == self._validate[
            'expected']

    def convert_types(self, i):
        self._values[i:] = self._validate['convert_function'](self._values[i:])

    @property
    def valid_first(self):
        if self.valid_length:
            return self._values[0] in self._validate['first']
        else:
            return False
