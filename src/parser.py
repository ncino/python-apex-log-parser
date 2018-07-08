from tokens import CodeUnit, SOQLQuery, Token

# Takes a LogReader instance and uses it to parse the subscriber log into
# tokens which can be consumed to do things like convert to json, etc.
class LogParser:

    def __init__(self, reader):
        self.reader = reader
        self.next_token = None
        self.get_next_token()
        
    def get_next_token(self):
        current_token = self.next_token
        self.next_token = self.parse_token()
        return current_token
    
    def has_more_tokens(self):
        return self.next_token != None

    def parse_token(self):
        token = None
        if (self.reader.has_more_lines()):
            text = self.reader.get_next_line()
            upper = text.upper()
            if ('CODE_UNIT_STARTED' in upper):
                token = CodeUnit(text, self)
            elif ('SOQL_EXECUTE_BEGIN' in upper):
                token = SOQLQuery(text, self)
            else:
                token = Token(text)
        return token