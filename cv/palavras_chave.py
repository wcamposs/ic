class PalavrasChave:
    def __init__(self):
        self.palavra_chave_1 = None
        self.palavra_chave_2 = None
        self.palavra_chave_3 = None
        self.palavra_chave_4 = None
        self.palavra_chave_5 = None
        self.palavra_chave_6 = None

    def parse(self, data):
        self.palavra_chave_1 = None
        self.palavra_chave_2 = None
        self.palavra_chave_3 = None
        self.palavra_chave_4 = None
        self.palavra_chave_5 = None
        self.palavra_chave_6 = None

    def __dict__(self):
        return {
            'palavra_chave_1': self.palavra_chave_1,
            'palavra_chave_2': self.palavra_chave_2,
            'palavra_chave_3': self.palavra_chave_3,
            'palavra_chave_4': self.palavra_chave_4,
            'palavra_chave_5': self.palavra_chave_5,
	        'palavra_chave_6': self.palavra_chave_6,
        }