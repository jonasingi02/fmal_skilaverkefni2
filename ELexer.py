import sys
from EToken import EToken


class ELexer:
    def __init__(self):
        self.token = EToken()
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
            return EToken(token, "PLUS")
        elif self.current_char == '-':
            token = self.current_char
            return EToken(token, "MINUS")
        elif self.current_char == '*':
            token = self.current_char
            return EToken(token, "MULT")
        elif self.current_char == '(':
            token = self.current_char
            return EToken(token, "LPAREN")
        elif self.current_char == ')':
            token = self.current_char
            return EToken(token, "RPAREN")
        elif self.current_char == '=':
            token = self.current_char
            return EToken(token, "ASSIGN")
        elif self.current_char == ';':
            token = self.current_char
            return EToken(token, "SEMICOL")
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
        return EToken(result, "INT")

    def tokenize_id(self):
        result = ''
        while self.current_char.isalpha():
            result += self.current_char
            if self.next_char.isalpha():
                self.read_char()
            else:
                break
        if result == 'end':
            return EToken(result, "END")
        elif result == 'print':
            return EToken(result, "PRINT")
        else:
            return EToken(result, "ID")

    def tokenize_keyword(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.read_char()
        if result == 'end':
            return EToken(result, "END")
        elif result == 'print':
            return EToken(result, "PRINT")
        else:
            return 'ID'

    def tokenize_error(self):
        token = self.current_char
        self.read_char()
        return f'ERROR: {token}'


if __name__ == "__main__":
    lexer = ELexer()

    while True:
        token = lexer.get_next_token()
        if token.token_type == "END":
            break
        print(token)