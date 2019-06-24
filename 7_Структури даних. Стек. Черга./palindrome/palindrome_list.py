from arraystack import ArrayStack


class Palindrome:
    """A class for Palindrome representation"""

    def __init__(self, file1, file2):
        self.write_file(file1, file2)

    def read_file(self, file1):
        """
        The function reads file and returns a list of palindromes

        """
        lst = []
        f = open(file1, encoding='utf-8', errors='ignore')
        for line in f:
            if self.palindrome_search(line.lower().split()[0]):
                lst.append(line)
        return lst

    @staticmethod
    def palindrome_search(line):
        """
        The function returns True if the word is a palindrome
        """
        s = ArrayStack()
        for letter in line:
            s.push(letter)
        reversed_line = ''
        while not s.isEmpty():
            reversed_line += s.pop()
        if line == reversed_line:
            return True
        else:
            return False

    def write_file(self, file1, file2):
        """
        The function tar writes all palindroms in file
        """
        f = open(file2, 'w', encoding='utf-8', errors='ignore')
        for word in self.read_file(file1):
            f.write(word)
        f.close()


if __name__ == "__main__":
    Palindrome('words.txt', 'palindrome_en.txt')
    Palindrome('base.lst', 'palindrome_uk.txt')
