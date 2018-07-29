class Disciplina:
    def __init__(self):
        self.sequencia_especificacao = None
        self.text = None

    def parse(self, data):
        self.sequencia_especificacao = None
        self.text = None

    def __dict__(self):
        return {
            'sequencia_especificacao': self.sequencia_especificacao,
            'text': self.text,
        }