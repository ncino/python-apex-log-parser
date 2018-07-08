import sys

from src.tokens import SOQLQuery
from src.reader import LogReader
from src.parser import LogParser
from src.writer import JsonWriter

# Main application entry point for the Apex Log Parser
# Execute by calling from the command line and supplying 
#   param1: path to an apex subscriber log file
#   param2: path to where a json output file should be generated
def parse(logfile, outfile):
    print('logfile: ' + logfile)
    print('outfile: ' + outfile)
    
    parser = LogParser(LogReader(logfile))
    writer = JsonWriter(outfile)
    writer.write_tree(parser)

    print('SQOL Queries: ' + str(SOQLQuery.total))

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print('ERROR: call must be of the form:')
        print('python main.py [log file path] [output file path]')
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        parse(arg1, arg2)