from EToken import EToken
from eparser import EParser
class SInterpreter:
    def __init__(self) -> None:
        self.parser = EParser()
        self.stack = []
        self.env = {}

    def cycle(self):
        while True:
            stdin = input() 
            if not stdin: 
                break
            token = self.parser.parse(stdin)  
            if not self.interpret(token):
                break
    
    def interpret(self, token: EToken):
        if token.token_code == EToken.INT:
            self.stack.append(int(token.lexeme))
        elif token.token_code == EToken.ID:
            self.stack.append(token.lexeme)
        elif token.token_code == EToken.ASSIGN:
            self.env[self.stack.pop()] = self.stack.pop()
        elif token.token_code == EToken.PLUS:
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif token.token_code == EToken.MINUS:
            self.stack.append(self.stack.pop() - self.stack.pop())
        elif token.token_code == EToken.MULT:
            self.stack.append(self.stack.pop() * self.stack.pop())
        elif token.token_code == EToken.PRINT:
            print(self.stack.pop())
        elif token.token_code == EToken.SEMICOL:
            pass
        elif token.token_code == EToken.END:
            return False
        elif token.token_code == EToken.ERROR:
            print(f"Error for operator: {token.token_code}")
            return False
        print()
        return True 