class Fraction():
    """Fraction Class"""
    
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self): #this method overides the default __str__ method built into python
       return str(self.num)+ "/"+ str(self.den)

    def gcd(self, m, n):
        while m % n != 0:
            oldm = m 
            oldn = n
            m = oldn
            n = oldm % oldn
       
        return n

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
       
        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, otherfraction):
       firstnum = self.num * otherfraction.den
       secondnum = otherfraction.num * self.den

       return firstnum == secondnum


f1 = Fraction(1,3) #invoke the class
f2 = Fraction(1,2)
print("----")
print(f1+f2)
print("----")
print(f1 == f2)
print('----')
print(f1.__str__())
print(f1) #Python knows the __str__ function will return this. 
print("----")