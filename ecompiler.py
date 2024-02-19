from EToken import EToken
from ELexer import ELexer
from eparser import EParser

lexer = ELexer()
parser = EParser(lexer)
parser.parse()