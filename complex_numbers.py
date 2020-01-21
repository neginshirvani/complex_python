import math


def coef(n):
    line = [1]

    for k in range(max(n, 0)):
        line.append(int(line[k] * (n - k) / (k + 1)))

    return line


def powers(n):
    lst = []

    for k in range(0, n + 1):
        lst.append(k)
    return lst


def power(a, b, n):
    line = coef(n)
    lst = powers(n)
    res = 0

    for i in range(len(line)):

        if lst[i] / 2 == 0:
            lst[i] = lst[i] * -1
        res += line[i] * pow(a, n) * pow(b, lst[i])
        n = n - 1

    return res


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
        return Carteziene(self.re, (-1) * self.im)

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
        return str(((self.re ** 2 + self.im ** 2)) ** (1 / 2)) + 'e^' + str(math.atan(self.im / self.re)) + 'i'

    def abs(self):
        return ((self.re ** 2 + self.im ** 2)) ** (1 / 2)

    def thieta(self):
        return math.atan(self.im / self.re)

    def power(self, n):
        return power(self.re, self.im, n)

    def root(self, n):
        return power(self.re, self.im, 1 / n)

    def exp(self):
        return pow(math.exp(self.re)) * pow(math.exp(self.im))

    def Ln(self):
        # return 'ln' + '(' + str(self.abs()) + ')' + '+' + str(self.thieta())
        return math.log(self.abs(), math.exp(1)) + self.thieta()

    def sin(self):
        return str((math.sin(self.re)*math.cosh(self.im))) + '+' + str((math.cos(self.re) + math.sinh(self.im))) + ' i'


    def cos(self):
        return str((math.cos(self.re)*math.cosh(self.im))) + '+' + str((math.sin(self.re) + math.sinh(self.im))) + ' i'




q = Carteziene(1, 1)
p = Carteziene(2, 2)

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
# print(p.thieta())
print(q.conjugate().to_string())
print(p.conjugate().to_string())
print(q.power(3))
print(p.power(2))
# print(d.to_polar())
print(q.Ln())
print(q.sin())
print(q.cos())

print(coef(3))
print(powers(3))
print(power(1, 2, 3))
