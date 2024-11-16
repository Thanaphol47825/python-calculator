class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return b - a

    def multiply(self, a, b):
        result = 0
        for _ in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b): # b/a
        if a == 0:
            return 0
        result = 0
        while b >= a:
            b = self.subtract(a, b)
            result += 1
        return result
        

    def modulo(self, a, b): # b%a
        if b == 0:
            return 0
        while b >= a:
            b = self.subtract(a, b)
        return b
        

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(11, 5))
    print("Example: modulo: ", calc.modulo(3, 10))