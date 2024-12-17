class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def division(self, a, b):
        return a / b
        
    def whoami(self):
        print ("am calculater")


class OddEven:
    def oddNumber(self, n):
        if n % 2 != 0:
            return f"{n} is an odd number"
        else:
            return f"{n} is not an odd number"

    def evenNumber(self, n):
        if n % 2 == 0:
            return f"{n} is an even number"
        else:
            return f"{n} is not an even number"
