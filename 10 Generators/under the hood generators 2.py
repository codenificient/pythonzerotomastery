# gen with only end
class pickRange():
    start = 5

    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if pickRange.start < self.end:
            intg = pickRange.start
            pickRange.start += 3
            return intg
        raise StopIteration


list1 = pickRange(43)
for u in list1:
    print(u)