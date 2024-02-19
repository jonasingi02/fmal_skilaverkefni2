from EToken import EToken
from ELexer import ELexer
from EParser import Eparser

lexer = ELexer()
parser = EParser(lexer)
parser.parse()