from document import *


def testDocument():
    print('Testing Document class...', end='')
    d = Document()
    d.insert('g')
    d.insert('a')
    d.insert('m')
    d.insert('m')
    d.insert('y')
    assert (d.string == "gammy")
    d.back()
    d.delete()
    d.insert('i')
    d.insert('n')
    d.insert('g')
    d.back()
    d.back()
    d.back()
    d.back()
    d.back()
    d.back()
    d.insert('r')
    d.back()
    d.back()
    d.insert('p')
    d.insert('r')
    d.insert('o')
    assert(d.string == "programming")
    assert (d.cursor.position == 3)
    d.back()
    d.back()
    d.back()
    assert (d.cursor.position == 0)
    d.back()
    assert (d.cursor.position == -1)
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.forward()
    d.insert('!')
    assert (d.string == "programming!")
    assert (d.cursor.position == 12)
    d.forward()
    assert (d.cursor.position == 13)
    d.back()
    d.back()
    d.filename = "test_document"
    d.save()
    file = open("test_document", "r")
    assert (file.read() == d.string)
    print('Passed!')

    try:
        d.delete()
    except IndexError:
        print('IndexError occurred while deleting non-existing symbol!\n')
    except ValueError:
        print('ValueError occurred while deleting non-existing symbol!!\n')

    try:
        d.save()
    except FileNotFoundError:
        print('FileNotFoundError occurred while saving file with no name!\n')


def testCursor():
    print('Testing Cursor class...', end='')
    d = Document()
    d.filename = "test_document"
    d.insert('m')
    d.insert('a')
    d.insert('t')
    d.insert('h')
    d.cursor.home()
    d.insert('L')
    d.insert('o')
    d.insert('e')
    d.cursor.back()
    d.insert('v')
    d.cursor.forward()
    d.insert(' ')
    assert (d.string == "Love math")
    assert (d.cursor.position == 5)
    d.cursor.home()
    assert (d.cursor.position == 0)
    d.cursor.end()
    assert (d.cursor.position == 9)
    print('Passed!')

def testCharacter():
    print('Testing Character class...', end='')
    d = Document()
    d.insert(str(Character('u', bold=True)))
    d.insert(str(Character('c', bold=True)))
    d.insert(str(Character('u', bold=True)))
    assert (d.string == "*u*c*u")
    d.cursor.home()
    d.delete()
    d.insert(str(Character('u', underline=True)))
    assert (d.string == "_u*c*u")
    d.cursor.back()
    d.insert(str(Character('c', italic=True)))
    d.insert(str(Character('s', italic=True)))
    d.insert(' ')
    assert (d.string == "/c/s _u*c*u")
    print('Passed!')

    for i in range(d.cursor.position + 1):
        try:
            d.cursor.back()
        except IndexError:
            print('IndexError occurred while moving cursor further than the beginning of the file!\n')

    for i in range(d.cursor.position + 1):
        try:
            d.cursor.forward()
        except IndexError:
            print('IndexError occurred while moving cursor further than the ending of the file!')


def testdocumentClasses():
    testDocument()
    testCursor()
    testCharacter()


testdocumentClasses()
