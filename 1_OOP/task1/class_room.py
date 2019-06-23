class Classroom():
    """Class for classroom representation."""
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment


    def __str__(self):
        """
        (Classroom)->(str)
        returns a volume and equipment of class.
         """
        return "Classroom {} has a capacity of {} \
persons and has the following equipment: {}.".format(self.number, self.capacity, ", ".join(self.equipment))
