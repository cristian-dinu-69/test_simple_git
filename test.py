class MathFunctions:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    

    def sub(self):
        return self.a - self.b
    

    def mul(self):
        return self.a * self.b
    

test1 = MathFunctions(1,20)
print(test1.a)
print(test1.b)
print(test1.add())
print(test1.sub())
print(test1.mul())
