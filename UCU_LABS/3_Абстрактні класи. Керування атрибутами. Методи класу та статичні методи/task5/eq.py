import math


class Polynomial:
    def __init__(self, polinomal_list, degrees=0):
        self.polinomal_list = list(polinomal_list).copy()
        self.degrees = degrees
        if len(self.polinomal_list) == self.polinomal_list.count(0):
            self.polinomal_list = []
        elif len(self.polinomal_list) != 0:
            for i in polinomal_list:
                if i == 0:
                    self.polinomal_list.remove(0)
                elif i != 0:
                    break

    def degree(self):
        self.degrees = len(self.polinomal_list[:-1])
        return self.degrees

    def coeff(self, coeficient):
        return self.polinomal_list[self.degrees - coeficient]

    def evalAt(self, x):
        sum = 0
        for i in range(len(self.polinomal_list)):
            sum += (self.polinomal_list[len(self.polinomal_list) -1 - i])*(x**i)
        return sum

    def __eq__(self, another):
        if isinstance(another, Polynomial):
            return self.polinomal_list == another.polinomal_list
        if len(self.polinomal_list) == 1:
            return self.polinomal_list[0] == another
        return False

    def __hash__(self):
        return hash(tuple(self.polinomal_list))

    def scaled(self, num):
        new_list = [i*num for i in self.polinomal_list]
        return Polynomial(new_list)

    def derivative(self):
        derivative_list = [self.polinomal_list[len(self.polinomal_list)- 1 - i] * i
                           for i in range(len(self.polinomal_list))][1:][::-1]
        return Polynomial(derivative_list)

    def addPolynomial(self, polynom):
        if not isinstance(polynom, Polynomial):
            return None
        if len(polynom.polinomal_list) > len(self.polinomal_list):
            lst = [0] * (len(polynom.polinomal_list) - len(self.polinomal_list)) + self.polinomal_list
            return Polynomial([x + y for x, y in zip(lst, polynom.polinomal_list)])
        if len(polynom.polinomal_list) <= len(self.polinomal_list):
            lst = [0] * (len(self.polinomal_list)-len(polynom.polinomal_list)) + polynom.polinomal_list
            return Polynomial([x + y for x, y in zip(lst, self.polinomal_list)])

    def multiplyPolynomial(self, polynom):
        if not isinstance(polynom, Polynomial):
            return None
        res = [0] * (len(self.polinomal_list) + len(polynom.polinomal_list) - 1)
        for o1, i1 in enumerate(self.polinomal_list):
            for o2, i2 in enumerate(polynom.polinomal_list):
                res[o1 + o2] += i1 * i2
        return Polynomial(res)

    def __repr__(self):
        return "Polynomial(coeffs={})".format(self.polinomal_list)


class Quadratic(Polynomial):
    def __init__(self, polinomal_list, disc=0, num=0):
        super().__init__(polinomal_list)
        self.disc = disc
        self.num = num

        if len(self.polinomal_list)!=3:
            assert False

    def discriminant(self):
        self.disc = self.polinomal_list[1]**2 - 4*self.polinomal_list[0]*self.polinomal_list[2]
        return self.disc

    def numberOfRealRoots(self):
        if self.disc > 0:
            self.num = 2
        elif self.disc < 0:
            self.num = 0
        elif self.disc == 0:
            self.num = 1
        return self.num

    def getRealRoots(self):
        if self.num == 2:
            q1 = (-self.polinomal_list[1] - math.sqrt(self.disc)) / (2 * self.polinomal_list[0])
            q2 = (-self.polinomal_list[1] + math.sqrt(self.disc)) / (2 * self.polinomal_list[0])
            lst_of_roots = [q1, q2]
        if self.num == 1:
            q1 = (-self.polinomal_list[1] - math.sqrt(self.disc)) / (2 * self.polinomal_list[0])
            lst_of_roots = [q1]
        if self.num == 0:
            lst_of_roots = [ ]
        return lst_of_roots

    def __repr__(self):
        return "Quadratic(a={}, b={}, c={})".format(self.polinomal_list[0], self.polinomal_list[1],
                                                    self.polinomal_list[2])
