# Defines functionality used by all types of log artifacts, these
# can be things like SOQL Queries, Code Units, Debug Statements, etc
class Token:

    def __init__(self, text):
        self.text = text
        self.segments = text.split('|')
        self.type = None if len(self.segments) < 2 else self.segments[1]

    def remove_line_endings(self, text):
        return text.replace('\n', '').replace('\r', '')

# Represents a logical boundary (method, trigger, workflow, etc) within
# an execution context. It can contain code units and other types of tokens.
class CodeUnit(Token):

    def __init__(self, text, parser):
        Token.__init__(self, text)
        self.source = self.remove_line_endings(self.segments[3 if len(self.segments) == 4 else 4])
        self.collect_tokens(parser)
        self.ownedqueries = self.count_owned_queries()

    def collect_tokens(self, parser):
        self.units = []
        self.soql = []
        collecting = parser.has_more_tokens()
        
        while collecting:
            token = parser.get_next_token()
            if (token.type == 'CODE_UNIT_FINISHED'):
                collecting = False
                break
            elif (isinstance(token, CodeUnit)):
                self.units.append(token)
            elif (isinstance(token, SOQLQuery)):
                self.soql.append(token)

    def count_owned_queries(self):
        count = len(self.soql)
        for sub in self.units:
            count = count + sub.count_owned_queries()
        return count

# Represents a SQOL Query execution and related information.
class SOQLQuery(Token):

    total = 0 #todo: build a better way to count queries

    def __init__(self, text, parser):
        Token.__init__(self, text)
        self.query = self.remove_line_endings(self.segments[4] if len(self.segments) == 5 else None)
        SOQLQuery.total = SOQLQuery.total + 1