class Document:
    """ Class for document representation """
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        (Document, str) -> NoneType
        The function inserts the character by the cursors` position
        """
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        (Document) -> NoneType
        The function delates the character by the cursors` position
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        (Document) -> NoneType
        The function saves the string to a file
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

    def forward(self):
        """
        (Document) -> NoneType
        The function moves the cursor forward on one position
        """
        self.cursor.position += 1

    def back(self):
        """
        (Document) -> NoneType
        The function moves the cursor back on one position
        """
        self.cursor.position -= 1

    @property
    def string(self):
        """
        (Document) -> str
        The function returns the string
        """
        return "".join(self.characters)


class Cursor:
    """ Class for cursor representation """
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """
        (Cursor) -> NoneType
        The function moves the cursor forward on one position
        """
        self.position += 1

    def back(self):
        """
        (Cursor) -> NoneType
        The function moves the cursor back on one position
        """
        self.position -= 1

    def home(self):
        """
        (Cursor) -> NoneType
        The function moves the cursor to the beginning of file
        """
        while self.document.characters[
                self.position-1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        """
        (Cursor) -> NoneType
        The function moves the cursor to the end of file
        """
        while self.position < len(self.document.characters
             ) and self.document.characters[self.position] != '\n':
            self.position += 1


class Character:
    """ Class for Character representation """
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        (Character) -> str
        The function returns the character in bold, italic and underline.
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

    def insert(self, character):
        """
        (Character, str) -> NoneType
        The function inserts the character by the cursors` position
        """
        if not hasattr(character, 'character'):
            self.character = Character(character)


    @property
    def string(self):
        """
        (Character) -> str
        The function returns the string
        """
        return "".join((str(c) for c in self.characters))

    def home(self):
        """
        (Character) -> NoneType
        The function moves the cursor to the beginning of file
        """
        while self.document.characters[self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """
        (Character) -> NoneType
        The function moves the cursor to the end of file
        """
        while self.position < len(
                self.document.characters) and \
                self.document.characters[
                    self.position
                ].character != '\n':
            self.position += 1
