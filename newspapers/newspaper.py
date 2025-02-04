from math import floor, ceil

class Newspaper():
    def __init__(self, max_width):
        assert(type(max_width) == int)
        assert(max_width >= 0)
        self.max_width = max_width
        self.lines = []

    def add_text_chunk(self, text_chunk):
        # Check that text chunk is of valid length
        assert(len(text_chunk) <= self.max_width)

        # If there are no lines yet or the text chunk does not fit on the previous line, add the chunk as a new line
        # Otherwise, add the chunk to the latest line.
        if len(self.lines) == 0 or len(self.lines[-1] + ' ' + text_chunk) > self.max_width:
            self.lines.append(text_chunk)
        else:
            self.lines[-1] += ' ' + text_chunk

    def _display_line(self, line):
        num_excess_spaces = self.max_width - len(line)

        num_padding_left = floor(num_excess_spaces / 2)
        num_padding_right = ceil(num_excess_spaces / 2)

        display_line = '*' + (' ' * num_padding_left) + line + (' ' * num_padding_right) + '*'

        return display_line

    def __str__(self):
        display_lines = []
        display_lines.append('*' * (self.max_width + 2))

        for line in self.lines:
            display_lines.append(self._display_line(line))

        display_lines.append('*' * (self.max_width + 2))

        return '\n'.join(display_lines)