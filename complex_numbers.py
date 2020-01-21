import math

class Carteziene:

    def __init__(self, re, im):
        self.re = re
        self.im = im

    def get_re(self):
        return self.re

    def get_im(self):
        return self.im

    def to_string(self):
        if self.im > 0:
            return str(self.re) + '+' + str(self.im) + 'i'
        else:
            return str(self.re) + str(self.im) + 'i'


    def conjugate(self):
        return Carteziene(self.re, (-1)*self.im)

    def add(self, other):
        return Carteziene(self.re + other.re, self.im + other.im)

    def sub(self, other):
        return Carteziene(self.re - other.re, self.im - other.im)

    def mul(self, other):
        return Carteziene(((self.re * other.re) - (self.im * other.im)),
                             ((self.re * other.im) + (other.re * self.im)))

    def div(self, other):
        return Carteziene((((self.re * other.re) + (self.im * other.im)) / (other.re ** 2 + other.im ** 2)),
                             (((other.re * self.im) - (self.re - other.im)) / (other.re ** 2 + other.im ** 2)))

    def to_polar(self):
        return str(((self.re**2 + self.im**2))**(1/2)) + 'e^' + str(math.atan(self.im/self.re)) + 'i'


    def abs(self):
        return ((self.re**2 + self.im**2))**(1/2)


    def thieta(self):
        return math.atan2(self.im/self.re)
    
    
    def power(self):
        return
    
    
    def root(self):
        return
    
    
    def exp(self):
        return
    
    def Ln(self):
        return
    
    def to_complex_power(self):
        return
    
    
    def sin(self):
        return
    
    
    def cos(self):
        return
    
    

class Function:
    
    






q = Carteziene(1, 1)
p = Carteziene(3, 4)

a = p.add(q)
b = q.sub(p)
c = p.mul(q)

print(q.to_polar())
print(p.to_string())
print(p.get_im())
print(p.get_re())
print(a.to_string())
print(b.to_string())
print(c.to_string())
print(p.thieta())
print(q.conjugate().to_string())
print(p.conjugate().to_string())
#print(d.to_polar())

