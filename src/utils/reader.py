class Reader():
    file = None

    def __init__(self, file):
        self.file = file

    def read(self):
        with open(self.file, 'r') as f:
            lines = f.readlines()
        return lines

    def split(self):
        lines = self.read()
        return [i.strip().split(",") for i in lines[1:]]

    def result(self):
        return self.split()


def read_and_split(all_orders):
    with open(all_orders, 'r') as f:
        lines = f.readlines()
        orders = [i.strip().split(",") for i in lines[1:]]
        return orders
