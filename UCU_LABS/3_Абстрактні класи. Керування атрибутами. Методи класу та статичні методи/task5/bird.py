class Bird:
    def __init__(self, bird_name, eggs_amount = 0):
        self.bird_name = bird_name
        self.eggs_amount = eggs_amount

    def fly(self):
        return "I can fly!"

    def countEggs(self):
        return self.eggs_amount

    def layEgg(self):
        self.eggs_amount += 1

    def __repr__(self):
        if self.eggs_amount == 1:
            return "{} has {} egg".format(self.bird_name, self.eggs_amount)
        return "{} has {} eggs".format(self.bird_name, self.eggs_amount)


class Penguin(Bird):
    def fly(self):
        return "No flying for me."

    def swim(self):
        return "I can swim!"


class MessengerBird(Bird):
    def __init__(self, bird_name, message=""):
        self.message = message
        super().__init__(bird_name)

    def deliverMessage(self):
        return self.message