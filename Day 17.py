class Calculator:
    def power(self, x, y):
        if (x < 0) or (y < 0):
            return("n and p should be non-negative")
        else:
            return x ** y