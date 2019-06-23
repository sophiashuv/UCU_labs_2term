from classroom import Classroom


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
print(classroom_016)
print(classroom_016.number)
print(classroom_016.capacity)
print(classroom_016.equipment)
print(classroom_016.is_larger(classroom_007))
print(classroom_016.equipment_differences(classroom_007))
print([classroom_016])
print(classroom_016)
