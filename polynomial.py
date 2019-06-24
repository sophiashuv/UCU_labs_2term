# Implementation of the Polynomial ADT using a sorted linked list.

class Polynomial :
    # Create a new polynomial object.
    def __init__(self, degree = None, coefficient = None):
        if degree is None :
            self._polyHead = None
        else :
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    # Return the degree of the polynomial.
    def degree(self):
        if self._polyHead is None :
            return -1
        else :
            return self._polyHead.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree :
            curNode = curNode.next

        if curNode is None or curNode.degree != degree :
            return 0.0
        else :
            return curNode.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        curNode = self._polyHead
        while curNode is not None :
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    # Polynomial addition: newPoly = self + rhsPoly.
    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Addition only allowed on non -empty polynomials."
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.
        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        # If self list contains more terms append them.
        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        # Or if rhs contains more terms append them.
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly

    # Polynomial subtraction: newPoly = self - rhsPoly.
    def __sub__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, "Addition only allowed on non -empty polynomials."
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        # Add corresponding terms until one list is empty.

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient*(-1)
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient*(-1)
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        # If self list contains more terms append them.
        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        # Or if rhs contains more terms append them.
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient*(-1))
            nodeB = nodeB.next
        return newPoly

    # Polynomial multiplication: newPoly = self * rhsPoly.
    def __mul__(self, rhsPoly):
        newPoly = Polynomial()
        nodeA = self._polyHead
        mixpoly = Polynomial()

        while nodeA is not None:
            nodeB = rhsPoly._polyHead
            while nodeB is not None:
                degree = nodeA.degree + nodeB.degree
                coefficient = nodeA.coefficient * nodeB.coefficient
                mixpoly._appendTerm(degree, coefficient)
                nodeB = nodeB.next
            nodeA = nodeA.next
        mixnode = mixpoly._polyHead

        for degree in range(-int(mixpoly.degree()), 1):
            degree = abs(degree)
            coef = 0
            while mixnode is not None:
                if mixnode.degree == degree:
                    coef += mixnode.coefficient
                mixnode = mixnode.next
            mixnode = mixpoly._polyHead
            newPoly._appendTerm(degree, coef)
        return newPoly

    def simple_add(self, rhsPoly):
        newPoly = Polynomial()
        if self.degree() > rhsPoly.degree():
            maxDegree = self.degree()
        else:
            maxDegree = rhsPoly.degree()

        i = maxDegree
        while i >= 0:
            value = self[i] + rhsPoly[i]
            newPoly._appendTerm(i, value)
            i += 1
        return newPoly

    # Helper method for appending terms to the polynomial.
    def _appendTerm(self, degree, coefficient) :
        if coefficient != 0.0 :
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None :
                self._polyHead = newTerm
            else :
                self._polyTail.next = newTerm
            self._polyTail = newTerm

    def __str__(self):
        node = self._polyHead
        s = ""
        while node is not None:
            if node.coefficient < 0.0:
                s += "({})*x^{} + ".format(node.coefficient, node.degree)
            else:
                s += "{}*x^{} + ".format(node.coefficient, node.degree)
            node = node.next
        return s[:-3]


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
