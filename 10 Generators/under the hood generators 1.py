class myGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if myGen.current < self.last:
            num = myGen.current
            myGen.current += 1
            return num
        raise StopIteration


gen = myGen(0, 100)
for i in gen:
    print(i)