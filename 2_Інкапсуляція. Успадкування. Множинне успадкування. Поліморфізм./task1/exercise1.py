class Building():
    """
    Class for building representation.
    """
    def __init__(self, building, address):
        self.building = building
        self.address = address


class House(Building):
    """
    Class for house representation.
    """
    def __init__(self, building, address, apartments_list):
        super().__init__(building, address)
        self.apartments_list = apartments_list


class AcademicBuilding(Building):
    ''' Class for classroom representation '''

    def __init__(self, address, classrooms):
        '''
        (Classroom, str, int, lst) -> NoneType
        Create new classroom
        '''
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        '''
        (AcademicBuilding) -> list
        returns list of all equipment in classrooms
        '''
        lst2 = []
        lst = [m for i in self.classrooms for m in i.equipment]
        for i in lst:
            tp = (str(i), lst.count(i))
            if tp not in lst2:
                lst2.append(tp)
        return lst2


    def  __repr__(self):
        '''
        (Classroom) -> str
        Return the string representation of the classroom
        '''
        line=""
        for room in self.classrooms:
            line += "{}".format(room) + "\n"
        return line

