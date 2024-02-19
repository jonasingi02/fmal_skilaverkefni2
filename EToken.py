class EToken:
    def __init__(self, lexeme, token_type):
        self.lexeme = lexeme
        self.token_type = token_type

    def __str__(self):
        return f"Lexeme: {self.lexeme}, Token type: {self.token_type}"
