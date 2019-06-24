from arrays import DynamicArray


class Encoder:
    def __init__(self, message):
        self.message = message

    def convert(self):
        """
        The function that returns array with angles that means the amount of degrees for which the line should move
        the line
        """
        start = 0
        new_arr = DynamicArray()
        for letter in self.message:
            lst = [ord(letter) // 16, ord(letter) % 16]
            for i in lst:
                angle = i * 22.5
                if start + angle < 360:
                    start += angle
                else:
                    start += angle - 360
                new_arr.append(start)
        return new_arr

    def __str__(self):
        """
        The function returns a string representing a message
        """
        st = "For encoding {} we need to move forward on  ".format(self.message)
        for i in self.convert():
            st += str(i) + "°, "
        return st[:-2]


if __name__ == "__main__":
    message = str(input("Enter a message which you want encode: "))
    mes = Encoder(message)
    mes.convert()
    print(mes)

