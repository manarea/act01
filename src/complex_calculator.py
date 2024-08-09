class ComplexCalculator:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def add(self, x):
        if x > 0:
            self.value += x
        elif x < 0:
            self.value -= abs(x)
        else:
            raise ValueError("Cannot add zero.")
        return self.value

    def subtract(self, x):
        if x > self.value:
            self.value = 0
        else:
            self.value -= x
        return self.value

    def multiply(self, x):
        if x == 0:
            raise ValueError("Cannot multiply by zero.")
        elif x < 0 and self.value < 0:
            self.value = abs(self.value * x)
        elif x < 0 or self.value < 0:
            self.value = -(abs(self.value) * abs(x))
        else:
            self.value *= x
        return self.value

    def divide(self, x):
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        elif self.value == 0:
            raise ValueError("Cannot divide when current value is zero.")
        else:
            self.value /= x
        return self.value

    def complex_operation(self, a, b):
        try:
            result = self.add(a) - self.subtract(b)
            if result < 0:
                result = self.multiply(result)
            else:
                result = self.divide(result)
        except ValueError as e:
            result = str(e)
        except ZeroDivisionError as e:
            result = str(e)
        return result
