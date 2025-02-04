from newspapers.newspaper import Newspaper

class NewspaperWithTitle(Newspaper):
    def __init__(self, max_width, title=''):
        super().__init__(max_width)
        self.set_title(title)

    def set_title(self, title):
        assert(len(title) <= self.max_width)
        self.title = title

    def __str__(self):
        title_header = '*' * (self.max_width + 2) + '\n' + self._display_line(self.title)

        return title_header + '\n' + super().__str__()