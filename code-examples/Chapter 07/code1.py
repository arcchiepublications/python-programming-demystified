class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Example usage
for number in CountDown(3):
    print(number)
