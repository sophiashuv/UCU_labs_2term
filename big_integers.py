class TwoWayNode(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class BigInteger:
    """Class for integer representation."""

    def __init__(self, initValue):
        """
        The function initialization a new instance.
        """
        if not initValue.startswith('-'):
            self.initValue = initValue.lstrip("0")
            if len(self.initValue) == 0:
                self.initValue = '0'
            self.sign = True
        else:
            self.sign = False
            self.initValue = initValue[1:].lstrip("-").lstrip("0")

        self.head = TwoWayNode(self.initValue[0])
        self.tail = self.head
        for i in range(1, len(self.initValue)):
            self.tail.next = TwoWayNode(self.initValue[i], prev=self.tail)
            self.tail = self.tail.next

    def toString(self):
        """
        The function return a string representation a BigInteger
        """
        return str(self)

    def into_bin(self):
        """
        The function return BigInteger converted into in binary
        """
        assert self >= BigInteger("0"), 'Must be naturlish'
        nums = [self]
        k = self
        while k > BigInteger("1"):
            k = k // BigInteger("2")
            nums.append(k)
        bits = ""
        for i in nums:
            bits += (str(0 if i % BigInteger("2") == BigInteger("0") else 1))
        return BigInteger(bits[::-1])

    def from_bin(self):
        """
        The function return BigInteger converted from in decsimal number
        """
        dec = 0
        n = 0
        for i in str(self)[::-1]:
            dec += 2 ** n * int(i)
            n += 1
        return BigInteger(str(dec))

    @staticmethod
    def plus_ost(rem, self_tail_data, rhsInt_tail_data):
        """
        The function for counting num and remainder while searching sum
        """
        num = int(self_tail_data) + int(rhsInt_tail_data) + rem
        if num >= 10:
            rem = 1
            num = num - 10
        else:
            rem = 0
        return num, rem

    @staticmethod
    def min_ost(rem, self_tail_data, rhsInt_tail_data):
        """
        The function for counting num and remainder while difference
        """
        if int(self_tail_data) < int(rhsInt_tail_data):
            self_tail_data = str(self_tail_data)
            self_tail_data += '1'
            self_tail_data = self_tail_data[::-1]
            num = int(self_tail_data) - int(rhsInt_tail_data) - rem
            rem = 1
        else:
            num = int(self_tail_data) - int(rhsInt_tail_data) - rem
            rem = 0
        if num < 0:
            num = 10 + num
            rem = 1
        return num, rem

    def __str__(self):
        """
        The function string representation of an BigInteger
        """
        head = self.head
        if self.sign is True:
            line = ''
        else:
            line = '-'
        for i in range(len(self)):
            line += head.data
            head = head.next
        return line

    def __int__(self):
        """
        The function returns int of BigInteger
        """
        return int(str(self))

    def __abs__(self):
        try:
            return BigInteger(str(abs(int(self))))
        except ValueError:
            return BigInteger("0")

    def __len__(self):
        """
        The function returns the len of BigInteger
        """
        length = 0
        head = self.head
        while head is not None:
            length += 1
            head = head.next
        return length

    def comparable(self, rhsInt, op):
        """
        The function returns operation
        """
        if op == ">":
            return self.__gt__(rhsInt)
        if op == ">=":
            return self.__ge__(rhsInt)
        if op == "<":
            return self.__lt__(rhsInt)
        if op == "<=":
            return self.__le__(rhsInt)
        if op == "==":
            return self.__eq__(rhsInt)
        if op == "!=":
            return self.__ne__(rhsInt)

    def bitwise_ops(self, rhsInt, operator):
        """
        The function returns  bitwise operations
        """
        if operator == "&":
            return self.__and__(rhsInt)
        if operator == "^":
            return self.__xor__(rhsInt)
        if operator == "|":
            return self.__or__(rhsInt)
        if operator == "<<":
            return self.__lshift__(rhsInt)
        if operator == ">>":
            return self.__rshift__(rhsInt)

    def arithmetic(self, rhsInt, op):
        """
        The function returns operation
        """
        if op == "+":
            return self.__add__(rhsInt)
        if op == "-":
            return self.__sub__(rhsInt)
        if op == "*":
            return self.__mul__(rhsInt)
        if op == "//":
            return self.__floordiv__(rhsInt)
        if op == "%":
            return self.__mod__(rhsInt)
        if op == "**":
            return self.__pow__(rhsInt)

    def __eq__(self, rhsInt):
        """
        The function returns True if self == rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign == rhsInt.sign:
            if len(self) == len(rhsInt):
                for i in range(len(self)):
                    if int(self_head.data) != int(rhsInt_head.data):
                        return False
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, rhsInt):
        """
        The function returns True if self != rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign == rhsInt.sign:
            if len(self) == len(rhsInt):
                for i in range(len(self)):
                    if int(self_head.data) != int(rhsInt_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                return False
            else:
                return True
        else:
            return True

    def __lt__(self, rhsInt):
        """
        The function returns True if self < rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign is False and rhsInt.sign is True:
            return True
        elif self.sign is True and rhsInt.sign is False:
            return False
        elif self.sign is True and rhsInt.sign is True:
            if len(self) < len(rhsInt):
                return True
            elif len(self) > len(rhsInt):
                return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return True
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return False
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                return False
        else:
            if len(self) < len(rhsInt):
                return False
            elif len(self) > len(rhsInt):
                return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return False
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                return False

    def __le__(self, rhsInt):
        """
        The finction returns True if self <= rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign is False and rhsInt.sign is True:
            return True
        elif self.sign is True and rhsInt.sign is False:
            return False
        elif self.sign is True and rhsInt.sign is True:
            if len(self) < len(rhsInt):
                return True
            elif len(self) > len(rhsInt):
                return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return True
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return False
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                else:
                    return True
        else:
            if len(self) < len(rhsInt):
                return False
            elif len(self) > len(rhsInt):
                return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return False
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                else:
                    return True

    def __gt__(self, rhsInt):
        """
        The function returns True if self > rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign is False and rhsInt.sign is True:
            return False
        elif self.sign is True and rhsInt.sign is False:
            return True
        elif self.sign is True and rhsInt.sign is True:
            if len(self) < len(rhsInt):
                return False
            elif len(self) > len(rhsInt):
                return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return False
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        rhsInt_head = rhsInt_head.next
                else:
                    return False
        else:
            if len(self) < len(rhsInt):
                return True
            elif len(self) > len(rhsInt):
                return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return True
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return False
                    else:
                        self.head = self.head.next
                        rhsInt_head = rhsInt_head.next
                else:
                    return False

    def __ge__(self, rhsInt):
        """
        The function returns True if self >= rhsInt
        """
        self_head = self.head
        rhsInt_head = rhsInt.head
        if self.sign is False and rhsInt.sign is True:
            return False
        elif self.sign is True and rhsInt.sign is False:
            return True
        elif self.sign is True and rhsInt.sign is True:
            if len(self) < len(rhsInt):
                return False
            elif len(self) > len(rhsInt):
                return True
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return False
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return True
                    else:
                        self_head = self_head.next
                        rhsInt.head = rhsInt.head.next
                else:
                    return True
        else:
            if len(self) < len(rhsInt):
                return True
            elif len(self) > len(rhsInt):
                return False
            else:
                for i in range(len(self)):
                    if int(self_head.data) < int(rhsInt_head.data):
                        return True
                    elif int(self_head.data) > int(rhsInt_head.data):
                        return False
                    else:
                        self_head = self_head.next
                        rhsInt.head = rhsInt.head.next
                else:
                    return True

    def __add__(self, rhsInt):
        """
        The function adds two BigInteders
        """
        sum = ""
        self_abs = abs(self)
        rhsInt_abs = abs(rhsInt)
        self_abs.sign = True
        rhsInt_abs.sign = True
        if self.sign is True and rhsInt.sign is True:
            self_tail = self.tail
            rhsInt_tail = rhsInt.tail
            rem = 0
            while self_tail is not None or rhsInt_tail is not None:
                if rhsInt_tail is None:
                    num, rem = self.plus_ost(rem, self_tail.data, 0)
                    self_tail = self_tail.prev
                elif self_tail is None:
                    num, rem = self.plus_ost(rem, 0, rhsInt_tail.data)
                    rhsInt_tail = rhsInt_tail.prev
                else:
                    num, rem = self.plus_ost(rem, self_tail.data, rhsInt_tail.data)
                    rhsInt_tail = rhsInt_tail.prev
                    self_tail = self_tail.prev
                sum += str(num)
            sum = sum[::-1]
            if rem == 1:
                res = BigInteger("1" + sum)
            else:
                res = BigInteger(sum)
            return res
        elif self.sign is True and rhsInt.sign is False:
            res = self_abs - rhsInt_abs
            if self_abs > rhsInt_abs:
                res.sign = True
            elif self_abs < rhsInt_abs:
                res.sign = False
            else:
                res = BigInteger('0')
            return res
        elif self.sign is False and rhsInt.sign is True:
            res = rhsInt_abs - self_abs
            if self_abs > rhsInt_abs:
                res.sign = False
            elif self_abs < rhsInt_abs:
                res.sign = True
            else:
                res = BigInteger('0')
            return res
        else:
            res = self_abs + rhsInt_abs
            res.sign = False
            return res

    def __sub__(self, rhsInt):
        """
        The function subs two BigInteders
        """
        self_abs = abs(self)
        rhsInt_abs = abs(rhsInt)
        subed = ""
        if self.sign is True and rhsInt.sign is True:
            if self > rhsInt:
                self_tail = self.tail
                rhsInt_tail = rhsInt.tail
                sign = True
            elif self < rhsInt:
                self_tail = rhsInt.tail
                rhsInt_tail = self.tail
                sign = False
            else:
                return BigInteger('0')
        elif self.sign is True and rhsInt.sign is False:
            res = self_abs + rhsInt_abs
            res.sign = True
            return res
        elif self.sign is False and rhsInt.sign is True:
            res = rhsInt_abs + self_abs
            res.sign = False
            return res
        else:
            if self_abs > rhsInt_abs:
                self_tail = self.tail
                rhsInt_tail = rhsInt.tail
                sign = False
            elif self_abs < rhsInt_abs:
                self_tail = rhsInt.tail
                rhsInt_tail = self.tail
                sign = True
            else:
                return BigInteger('0')
        rem = 0
        while self_tail is not None or rhsInt_tail is not None:
            if rhsInt_tail is None:
                num, rem = self.min_ost(rem, self_tail.data, 0)
                self_tail = self_tail.prev
            elif self_tail is None:
                num, rem = self.min_ost(rem, 0, rhsInt_tail.data)
                rhsInt_tail = rhsInt_tail.prev
            else:
                num, rem = self.min_ost(rem, self_tail.data, rhsInt_tail.data)
                rhsInt_tail = rhsInt_tail.prev
                self_tail = self_tail.prev
            subed += str(num)
        res = BigInteger(subed[::-1])
        res.sign = sign
        return res

    def __mul__(self, rhsInt):
        """
        The function multiplies two BigInteders
        """
        multiplied = BigInteger('0')
        one = 0
        self_end = self.tail
        while self_end is not None:
            rhsInt_end = rhsInt.tail
            two = 0
            while rhsInt_end is not None:
                multiplied += BigInteger(str((int(self_end.data) * int(rhsInt_end.data))*10**(one + two)))
                two += 1
                rhsInt_end = rhsInt_end.prev
            one += 1
            self_end = self_end.prev
        if self.sign == rhsInt.sign:
            multiplied.sign = True
        else:
            multiplied.sign = False
        return multiplied

    def __floordiv__(self, rhsInt):
        """
        The function returns the largest int value that is less than or equal
        to the algebraic quotient
        """
        assert rhsInt != BigInteger("0"), "Division by zero is not possible"
        self_abs = abs(self)
        rhsInt_abs = abs(rhsInt)
        self_abs.sign = True
        rhsInt_abs.sign = True
        div = BigInteger("0")
        if self_abs == rhsInt_abs:
            if self.sign == rhsInt.sign:
                div += BigInteger("1")
            else:
                div += BigInteger("-1")
        else:
            while self_abs > rhsInt_abs:
                self_abs -= rhsInt_abs
                div += BigInteger("1")
            if self_abs == rhsInt_abs:
                div += BigInteger("1")
            if self.sign == rhsInt.sign:
                div.sign = True
            else:
                div += BigInteger("1")
                div.sign = False
        return div

    def __mod__(self, rhsInt):
        """
        The function return the reminder of a division
        """
        assert rhsInt != BigInteger("0"), "Division by zero is not possible"
        res = self - (self // rhsInt) * rhsInt
        return res

    def __pow__(self, power):
        """
        The function takes power
        """
        assert power != BigInteger("0"), "Division by zero is not possible"
        if power == BigInteger("1"):
            return self
        else:
            return self.__pow__(power-BigInteger("1"))*self

    def __and__(self, rhsInt):
        """
        The function returns binary and between two BigIntegers
        """
        res = ""
        self_bin = self.into_bin()
        rhsInt_bin = rhsInt.into_bin()
        self_tail = self_bin.tail
        rhsInt_tail = rhsInt_bin.tail
        while self_tail is not None or rhsInt_tail is not None:
            if rhsInt_tail is None:
                num = 0
                res += str(num)
                self_tail = self_tail.prev
            elif self_tail is None:
                num = 0
                res += str(num)
                rhsInt_tail = rhsInt_tail.prev
            else:
                num = int(self_tail.data) * int(rhsInt_tail.data)
                res += str(num)
                self_tail = self_tail.prev
                rhsInt_tail = rhsInt_tail.prev
        return BigInteger(res[::-1]).from_bin()

    def __or__(self, rhsInt):
        """
        The function returns binary or between two BigIntegers
        """
        res = ""
        self_bin = self.into_bin()
        rhsInt_bin = rhsInt.into_bin()
        self_tail = self_bin.tail
        rhsInt_tail = rhsInt_bin.tail
        while self_tail is not None or rhsInt_tail is not None:
            if rhsInt_tail is None:
                num = int(self_tail.data)
                res += str(num)
                self_tail = self_tail.prev
            elif self_tail is None:
                num = int(rhsInt_tail.data)
                res += str(num)
                rhsInt_tail = rhsInt_tail.prev
            else:
                if int(self_tail.data) + int(rhsInt_tail.data) > 0:
                    num = 1
                else:
                    num = 0
                res += str(num)
                self_tail = self_tail.prev
                rhsInt_tail = rhsInt_tail.prev
        return BigInteger(res[::-1]).from_bin()

    def __xor__(self, rhsInt):
        """
        The function returns binary xor between two BigIntegers
        """
        res = ""
        self_bin = self.into_bin()
        rhsInt_bin = rhsInt.into_bin()
        self_tail = self_bin.tail
        rhsInt_tail = rhsInt_bin.tail
        while self_tail is not None or rhsInt_tail is not None:
            if rhsInt_tail is None:
                if int(self_tail.data) == 0:
                    num = 0
                else:
                    num = 1
                res += str(num)
                self_tail = self_tail.prev
            elif self_tail is None:
                if int(rhsInt_tail.data) == 0:
                    num = 0
                else:
                    num = 1
                res += str(num)
                rhsInt_tail = rhsInt_tail.prev
            else:
                if int(rhsInt_tail.data) == int(self_tail.data):
                    num = 0
                else:
                    num = 1
                res += str(num)
                self_tail = self_tail.prev
                rhsInt_tail = rhsInt_tail.prev
        return BigInteger(res[::-1]).from_bin()

    def __rshift__(self, rhsInt):
        """
        Thw function returns binary >> between two BigIntegers
        """
        return BigInteger(str(self // BigInteger(str(2 ** int(rhsInt)))))

    def __lshift__(self, rhsInt):
        """
        Thw function returns binary << between two BigIntegers
        """
        return BigInteger(str(self * BigInteger(str(2 ** int(rhsInt)))))
