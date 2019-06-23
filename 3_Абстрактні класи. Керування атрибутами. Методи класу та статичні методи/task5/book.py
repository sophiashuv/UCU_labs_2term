class Book:
    def __init__(self, book_name, book_author, num_pages, current_page=1, book_mark=None):
        self.book_name = book_name
        self.book_author = book_author
        self.num_pages = num_pages
        self.current_page = current_page
        self.book_mark = book_mark


    def turnPage(self, page):
        if self.current_page == 1 and page == -1:
            self.current_page = 1
        elif self.current_page + page < self.num_pages:
            self.current_page += page
        else:
            self.current_page = self.num_pages

    def getCurrentPage(self):
        return self.current_page

    def placeBookmark(self):
        self.book_mark = self.current_page

    def getBookmarkedPage(self):
        return self.book_mark

    def turnToBookmark(self):
        if self.book_mark is not None:
            self.current_page = self.book_mark

    def removeBookmark(self):
        self.book_mark = None

    def __eq__(self, another):
        if isinstance(self, Book):
            return self.book_name == another.book_name and self.book_author == another.book_author and \
                   self.num_pages == another.num_pages and self.current_page == another.current_page and \
                   self.book_mark == another.book_mark
        return False

    def __str__(self):
        if self.num_pages == 1 and self.book_mark is None:
            return 'Book<{0} by {1}: {2} page,' \
                   ' currently on page {3}>'.format(self.book_name,
                                                    self.book_author, str(self.num_pages), str(self.current_page))
        elif self.num_pages > 1 and self.book_mark is None:
            return 'Book<{0} by {1}: {2} pages,' \
                   ' currently on page {3}>'.format(self.book_name,
                                                    self.book_author, str(self.num_pages), str(self.current_page))
        elif self.num_pages == 1 and self.book_mark is not None:
            return 'Book<{0} by {1}: {2} page,' \
                   ' currently on page {3},' \
                   ' page {4} bookmarked>'.format(self.book_name,
                                                  self.book_author, str(self.num_pages), str(self.current_page),
                                                  str(self.book_mark))
        elif self.num_pages > 1 and self.book_mark is not None:
            return 'Book<{0} by {1}: {2} pages,' \
                   ' currently on page {3}, page {4} bookmarked>'.format(self.book_name,
                                                                         self.book_author, str(self.num_pages),
                                                                         str(self.current_page), str(self.book_mark))

