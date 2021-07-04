class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, input_num):
        self.value -= input_num

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self,num):
        self.value += num
        if self.value > 100:
            self.value = 100


cal2 = MaxLimitCalculator()
cal2.add(40)
cal2.add(492)
print(cal2.value)

