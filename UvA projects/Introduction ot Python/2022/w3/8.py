
"""
Modify the Calculator class below to include an integer attribute called
'base_number'. The value of this attribute should be passed to the class at the
time of object construction.

In addition, add four methods to your class as follows:
1. The 'add' method returns the sum of 'base_number' and 10.
2. The 'sub' method returns the difference between 'base_number' and 20.
3. The 'mul' method returns the multiplicative product of 'base_number' and 30.
4. The 'intdiv' method returns the result of the integer division of
   'base_number' by 40.

Each method above should return an integer.

For example:
If we create an object from your class as:
my_calculator = Calculator(199)
then the method call my_calculator.intdiv() should return the integer:
4
"""
class Calculator:
    def __init__(self, base_number):
        self.result = 0
        self.test = base_number
        
    def add(self):
        self.result += 10 + self.test
        return self.result

    def sub(self):
        self.result = self.test - 20
        return self.result

    def mul(self):
        self.result = self.test*30
        return self.result

    def intdiv(self):
        self.result = self.test/40
        return self.result

my_calculator = Calculator(71)

print(my_calculator.sub())