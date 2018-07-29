class Instituicao:
    def __init__(self):
        self.codigo = None
        self.nome = None
        self.sigla = None
        self.sigla_uf = None
        self.sigla_pais = None
        self.nome_pais = None
        self.flag_agencia_fomento = None
        self.flag_instituicao_ensino = None

    def parse(self, data):
        self.codigo = data.get('CODIGO-INSTITIUICAO')
        self.nome = data.get('NOME-INSTITUICAO')
        self.sigla = data.get('SIGLA-INSTITUICAO')
        self.sigla_uf = data.get('SIGLA-UF-INSTITUICAO')
        self.sigla_pais = data.get('SIGLA-PAIS-INSTITUICAO')
        self.nome_pais = data.get('NOME-PAIS-INSTITUICAO')
        self.flag_agencia_fomento = data.get('FLAG-AGENCIA-FOMENTO')
        self.flag_instituicao_ensino = data.get('FLAG-INSTITUICAO-DE-ENSINO')

    def __dict__(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'sigla': self.sigla,
            'sigla_uf': self.sigla_uf,
            'sigla_pais': self.sigla_pais,
            'nome_pais': self.nome_pais,
            'flag_agencia_fomento': self.flag_agencia_fomento,
            'flag_instituicao_ensino': self.flag_instituicao_ensino,
        }
