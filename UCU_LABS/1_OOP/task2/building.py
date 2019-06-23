import classroom
import doctest

class AcademicBuilding():
    ''' Class for classroom representation '''


    def __init__(self, address, classrooms):
        '''
        (Classroom, str, int, lst) -> NoneType
        Create new classroom
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        '''
        self.address = address
        self.classrooms = classrooms


    def total_equipment(self):
        '''
        (AcademicBuilding) -> list
        returns list of all equipment in classrooms
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('projector', 2), ('mic', 1), ('TV', 1)]
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
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        <BLANKLINE>
        '''
        line=""
        for room in self.classrooms:
            line += "{}".format(room) + "\n"
        return line


if __name__ == "__main__":
    doctest.testmod()
