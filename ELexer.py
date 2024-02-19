import sys
from EToken import EToken


class ELexer:
    def __init__(self):
        self.current_char = None
        self.next_char = None
    def get_next_token(self):
        self.read_char()

        while self.current_char == None:
            self.read_char()
        while self.current_char == ' ':
            self.read_char()

        if self.current_char.isdigit():
            return self.tokenize_int()
        elif self.current_char.isalpha():
            return self.tokenize_id()
        elif self.current_char == '+':
            token = self.current_char
            return EToken(token, EToken.PLUS)
        elif self.current_char == '-':
            token = self.current_char
            return EToken(token, EToken.MINUS)
        elif self.current_char == '*':
            token = self.current_char
            return EToken(token, EToken.MULT)
        elif self.current_char == '(':
            token = self.current_char
            return EToken(token, EToken.LPAREN)
        elif self.current_char == ')':
            token = self.current_char
            return EToken(token, EToken.RPAREN)
        elif self.current_char == '=':
            token = self.current_char
            return EToken(token, EToken.ASSIGN)
        elif self.current_char == ';':
            token = self.current_char
            return EToken(token, EToken.SEMICOL)
        else:
            return self.tokenize_error()

    def read_char(self):
        self.current_char = self.next_char
        self.next_char = sys.stdin.read(1)

    def tokenize_int(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            if self.next_char.isdigit():
                self.read_char()
            else:
                break
        return EToken(result, EToken.INT)

    def tokenize_id(self):
        result = ''
        while self.current_char.isalpha():
            result += self.current_char
            if self.next_char.isalpha():
                self.read_char()
            else:
                break
        if result == 'end':
            return EToken(result, EToken.END)
        elif result == 'print':
            return EToken(result, EToken.PRINT)
        else:
            return EToken(result, EToken.ID)

    def tokenize_error(self):
        token = self.current_char
        self.read_char()
        return f'ERROR: {token}'
