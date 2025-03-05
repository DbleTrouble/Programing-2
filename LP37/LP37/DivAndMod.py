
class DivAndMod:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self._div = 0
        self._mod = 0
        
    def calc(self):
        self._div = self.num1 / self.num2
        self._mod = self.num1 % self.num2
        
    def get_div(self):
        return self._div
    
    def get_mod(self):
        return self._mod
    
    def get_divmod(self):
        return self._div, self._mod
    
