import sys
import EToken


class ELexer:
    def __init__(self):
        self.current_char = None

    def get_next_token(self):
        self.read_char()

        while self.current_char and self.current_char == ' ':
            self.read_char()

        if self.current_char.isdigit():
            return self.tokenize_int()
        elif self.current_char.isalpha():
            return self.tokenize_id()
        elif self.current_char == '+':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == '-':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == '*':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == '(':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == ')':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == '=':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char == ';':
            token = self.current_char
            self.read_char()
            return token
        elif self.current_char.isalpha():
            return self.tokenize_keyword()
        elif not self.current_char:
            return None
        else:
            return self.tokenize_error()

    def read_char(self):
        self.current_char = sys.stdin.read(1)

    def tokenize_int(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.read_char()
        return EToken(result, "INT")

    def tokenize_id(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.read_char()
        return EToken(result, "ID")

    def tokenize_keyword(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.read_char()
        if result == 'end':
            return EToken('END', "END")
        elif result == 'print':
            return 'PRINT'
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
        if token is None:
            break
        print(token)