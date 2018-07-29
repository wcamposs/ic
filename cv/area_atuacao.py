class AreaAtuacao:
    def __init__(self):
        self.sequencia = None
        self.grande_area_conhecimento = None
        self.area_conhecimento = None
        self.sub_area_conhecimento = None
        self.especialidade = None

    def parse(self, data):
        self.sequencia = data.get('SEQUENCIA')
        self.grande_area_conhecimento = data.get('NOME-GRANDE-AREA-DO-CONHECIMENTO')
        self.area_conhecimento = data.get('NOME-DA-AREA-DO-CONHECIMENTO')
        self.sub_area_conhecimento = data.get('NOME-DA-SUB-AREA-DO-CONHECIMENTO')
        self.especialidade = data.get('NOME-DA-ESPECIALIDADE')

    def __dict__(self):
        return {
            'sequencia': self.sequencia,
            'grande_area_conhecimento': self.grande_area_conhecimento,
            'area_conhecimento': self.area_conhecimento,
            'sub_area_conhecimento': self.sub_area_conhecimento,
            'especialidade': self.especialidade,
        }
