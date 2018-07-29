class Idioma:
    def __init__(self):
        self.idioma = None
        self.descricao = None
        self.proficiencia_fala = None
        self.proficiencia_leitura = None
        self.proficiencia_escrita = None
        self.proficiencia_compreensao = None

    def parse(self, data):
        self.idioma = None
        self.descricao = None
        self.proficiencia_fala = None
        self.proficiencia_leitura = None
        self.proficiencia_escrita = None
        self.proficiencia_compreensao = None

    def __dict__(self):
        return {
            'idioma': self.idioma,
            'descricao': self.descricao,
            'proficiencia_fala': self.proficiencia_fala,
            'proficiencia_leitura': self.proficiencia_leitura,
            'proficiencia_escrita': self.proficiencia_escrita,
	    'proficiencia_compreensao': self.proficiencia_compreensao,
        }
