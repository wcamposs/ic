class AreasDoConhecimento:
    def __init__(self):
        self.nome_grande_area_do_conhecimento = None
        self.nome_da_area_do_conhecimento = None
        self.nome_da_sub_area_do_conhecimento = None
        self.nome_da_especialidade = None

    def parse(self, data):
        self.nome_grande_area_do_conhecimento = None
        self.nome_da_area_do_conhecimento = None
        self.nome_da_sub_area_do_conhecimento = None
        self.nome_da_especialidade = None

    def __dict__(self):
        return {
            'nome_grande_area_do_conhecimento': self.nome_grande_area_do_conhecimento,
            'nome_da_area_do_conhecimento': self.nome_da_area_do_conhecimento,
            'nome_da_sub_area_do_conhecimento': self.nome_da_sub_area_do_conhecimento,
            'nome_da_especialidade': self.nome_da_especialidade,
        }