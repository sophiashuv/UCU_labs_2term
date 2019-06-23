import doctest


class Classroom():
    ''' Class for classroom representation '''


    def __init__(self, number, capacity, equipment):
        '''
        (Classroom, str, int, lst) -> NoneType
        Create new classroom
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        '''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment


    def __str__(self):
        '''
        (Classroom) -> str
        Return the string representation of the classroom
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        '''
        return "Classroom {} has a capacity of {} \
persons and has the following equipment: {}.".format(self.number, self.capacity, ", ".join(self.equipment))


    def is_larger(self, room):
        '''
        (Classroom, Classroom) -> bool
        Return True if the capacity of Classroom1 is larger then capacity of Classroom2
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        '''
        if self.capacity >= room.capacity:
            return True
        else:
            return False


    def equipment_differences(self, room):
        '''
        (Classroom1, Classroom2) -> list
        Return the list of equipment in Classroom1 which aren't in Classroom2
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        '''
        return [i  for i in self.equipment if i not in room.equipment]


    def __repr__(self):
        '''
        (Classroom) -> str
        Return the string representation of the classroom
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        '''
        return "Classroom('{}', {}, {})".format(self.number, self.capacity, self.equipment)


if __name__ == "__main__":
    doctest.testmod()