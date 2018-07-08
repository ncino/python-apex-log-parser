import os

from tokens import CodeUnit, SOQLQuery

# Quick and dirty JSON writer for Subscriber Log tokens. 
class JsonWriter:

    def __init__(self, path):
        self.file = path

    def serialize_query(self, token, index):
        json = ', {' if index > 0 else '{'
        json = json + '"query": "' + token.query + '"' 
        json = json + '}'
        return json

    def serialize_code_unit(self, token, index):
        json = ', {' if index > 0 else '{'
        json = json + '"source": "' + token.source + '", '
        json = json + '"ownedqueries": "' + str(token.ownedqueries) + '", '
        json = json + '"units": ['
        index = 0
        for unit in token.units:
            json = json + self.serialize_code_unit(unit, index)
            index = index + 1
        json = json + '], "queries": ['
        index = 0
        for query in token.soql:
            json = json + self.serialize_query(query, index)
            index = index + 1
        json = json + ']}'
        return json

    def write_tree(self, parser):
        json = '['
        index = 0
        while parser.has_more_tokens():
            token = parser.get_next_token()
            if (isinstance(token, CodeUnit)):
                json = json + self.serialize_code_unit(token, index)
                index = index + 1
            if (isinstance(token, SOQLQuery)):
                json = json + self.serialize_query(token, index)
                index = index + 1
        json = json + ']'
        self.write_to_file(json)
    
    def write_to_file(self, json):
        if os.path.exists(self.file): os.remove(self.file)
        f = open(self.file, 'w+')
        f.write(json)
        f.close()