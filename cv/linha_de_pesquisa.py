class LinhaDePesquisa:
    def __init__(self):
        self.sequencia_linha = None
        self.titulo_da_linha_de_pesquisa = None
        self.flag_linha_de_pesquisa_ativa = None
        self.objetivos_linha_de_pesquisa = None
        self.titulo_da_linha_de_pesquisa_ingles = None
        self.objetivos_linha_de_pesquisa_ingles = None

    def parse(self, data):
        self.sequencia_linha = None
        self.titulo_da_linha_de_pesquisa = None
        self.flag_linha_de_pesquisa_ativa = None
        self.objetivos_linha_de_pesquisa = None
        self.titulo_da_linha_de_pesquisa_ingles = None
        self.objetivos_linha_de_pesquisa_ingles = None

    def __dict__(self):
        return {
            'sequencia_linha': self.sequencia_linha,
            'titulo_da_linha_de_pesquisa': self.titulo_da_linha_de_pesquisa,
            'flag_linha_de_pesquisa_ativa': self.flag_linha_de_pesquisa_ativa,
            'objetivos_linha_de_pesquisa': self.objetivos_linha_de_pesquisa,
            'titulo_da_linha_de_pesquisa_ingles': self.titulo_da_linha_de_pesquisa_ingles,
	        'objetivos_linha_de_pesquisa_ingles': self.objetivos_linha_de_pesquisa_ingles,
        }