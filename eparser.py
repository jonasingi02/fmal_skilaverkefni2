from ELexer import ELexer

class EParser():

    def __init__(self):
        self.lexer = ELexer()
        self.interCode = []
        self.curr_token = None

    def parse(self):
        self.curr_token = self.next_token()
        self.statements()

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token == EToken.ERROR: # lexical error
            self.error()   
        
    def statements(self):
        self.parse()
        self.get_next_token()
        while(self.next_token == ";"):
            self.parse()
        self.validate_token("end")

    def statement(self):
        self.get_next_token()
        if self.validate_token('print'):
            self.get_next_token()
            var = self.validate_token('id')
            if (var):
                var = self.next_token
            self.interCode.append(f'PUSH {var}')
            self.interCode.append('PRINT')
        elif self.validate_token("id"):
            if self.next_token == 'end':
                pass
            else:
                var = self.next_token
                self.get_next_token()
                self.validate_token('=')
                self.get_next_token()
                self.expr()
                self.interCode.append(f'ASSIGN')
                self.interCode.append(f'PUSH {var}')
        else:
            raise SyntaxError(f'Unexpected token: {self.next_token}')

    def expr(self):
        self.term()
        while self.next_token in ('+', '-'):
            op = self.next_token
            self.get_next_token()
            self.term()
            if op == '+':
                self.interCode.append('ADD')
            elif op == '-':
                self.interCode.append('SUB')

    def term(self):
        self.factor()
        while self.next_token == '*':
            self.get_next_token()
            self.factor()
            self.interCode.append('MULT')

    def factor(self):
        if self.validate_token('int'):
            value = self.next_token
            self.interCode.append(f'PUSH {value}')
            self.get_next_token()
        elif self.next_token == 'id':
            var = self.next_token
            self.interCode.append(f'PUSH {var}')
            self.get_next_token()
        elif self.next_token == '(':
            self.get_next_token()
            self.expr()
            self.validate_token(')')
            self.get_next_token()
        else:
            raise SyntaxError(f'Unexpected token: {self.next_token}')
        

def isinteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
        
input_str = "print x ; y = 5 + ( 3 * 2 ) ; end"
generator = intermediateCodeGenerator()
generator.main(input_str)

for code_line in generator.interCode:
    print(code_line)