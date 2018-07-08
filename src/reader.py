# Provides a mechanism to iterate over the log in a line-by-line fashion.
# Used by the LogParser mainly for tokenization purposes.
class LogReader:

    def __init__(self, filePath):
        self.lines = []
        self.index = 0
        with open(filePath, 'r') as file:
            self.lines = file.readlines()
            self.lineCount = len(self.lines)

    def get_next_line(self):
        line = None
        if (self.has_more_lines()):
            line = self.lines[self.index]
            self.index = self.index + 1
        return line

    def has_more_lines(self):
        return self.index < self.lineCount