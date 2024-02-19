import sys
from ELexer import ELexer, EToken

class EParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.interCode = []
        self.current_token = None

    def parse(self):
        self.current_token = self.next_token()
        self.statements()

    def next_token(self):
        return self.lexer.get_next_token()

    def statements(self):
        self.statement()
        while self.current_token.token_code == EToken.SEMICOL:
            self.next_token()
            self.statement()

    def statement(self):
        if self.current_token.token_code == EToken.PRINT:
            self.next_token()
            self.expr()
        elif self.current_token.token_code == EToken.ID:
            self.next_token()
            if self.current_token and self.current_token.token_code == EToken.ASSIGN:
                self.next_token()
                self.expr()

    def expr(self):
        self.term()
        while self.current_token.token_code in (EToken.PLUS, EToken.MINUS):
            op = self.current_token.lexeme
            self.next_token()
            self.term()
            if op == '+':
                self.interCode.append('ADD')
            elif op == '-':
                self.interCode.append('SUB')

    def term(self):
        self.factor()
        while self.current_token and self.current_token.token_code == EToken.MULT:
            self.next_token()
            self.factor()
            self.interCode.append('MULT')

    def factor(self):
        if self.current_token and self.current_token.token_code == EToken.INT:
            value = self.current_token.lexeme
            self.interCode.append(f'PUSH {value}')
            self.next_token()
        elif self.current_token and self.current_token.token_code == EToken.ID:
            var = self.current_token.lexeme
            self.interCode.append(f'PUSH {var}')
            self.next_token()
        elif self.current_token and self.current_token.token_code == EToken.LPAREN:
            self.next_token()
            self.expr()
            if self.current_token and self.current_token.token_code == EToken.RPAREN:
                self.next_token()
            else:
                raise SyntaxError("Expected ')' but got end of input")
        else:
            raise SyntaxError(f'Unexpected token: {self.current_token.lexeme}')

    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        