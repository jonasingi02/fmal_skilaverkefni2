from EToken import EToken
from eparser import EParser
class SInterpreter:
    def __init__(self) -> None:
        self.stack = []
        self.env = {}
        pass

    def cycle():
        pass
    
    def interpret(self, token):
        if token.token_type == EToken.INT:
            self.stack.append(int(token.lexeme))
        elif token.token_type == EToken.ID:
            self.stack.append(token.lexeme)
        elif token.token_type == EToken.ASSIGN:
            self.env[self.stack.pop()] = self.stack.pop()
        elif token.token_type == EToken.PLUS:
            self.stack.append(self.stack.pop() + self.stack.pop())
        elif token.token_type == EToken.MINUS:
            self.stack.append(self.stack.pop() - self.stack.pop())
        elif token.token_type == EToken.MULT:
            self.stack.append(self.stack.pop() * self.stack.pop())
        elif token.token_type == EToken.PRINT:
            print(self.stack.pop())
        elif token.token_type == EToken.SEMICOL:
            pass
        elif token.token_type == EToken.END:
            return False
        elif token.token_type == EToken.ERROR:
            print("Error: Unrecognized token")
            return False
        return True 