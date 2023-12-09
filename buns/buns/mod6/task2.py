class DoubleElement:
    def __init__(self, *lst):
        self.data = list(lst)
        self.index = 0

    def __next__(self):
        if self.index < len(self.data):
            first = self.data[self.index]
            self.index += 1
            if self.index < len(self.data):
                second = self.data[self.index]
            else:
                second = None
            return (first, second)
        raise StopIteration

    def __iter__(self):
        self.index = 0
        return self

dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
