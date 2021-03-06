class DirecaoEAdministracao:
    def __init__(self):
        self.sequencia_funcao_atividade = None
        self.flag_periodo = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_unidade = None
        self.formato_cargo_ou_funcao = None
        self.cargo_ou_funcao = None
        self.nome_unidade = None
        self.cargo_ou_funcao_ingles = None

    def parse(self, data):
        self.sequencia_funcao_atividade = None
        self.flag_periodo = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_unidade = None
        self.formato_cargo_ou_funcao = None
        self.cargo_ou_funcao = None
        self.nome_unidade = None
        self.cargo_ou_funcao_ingles = None

    def __dict__(self):
        return {
            'sequencia_funcao_atividade': self.sequencia_funcao_atividade,
            'flag_periodo': self.flag_periodo,
            'mes_inicio': self.mes_inicio,
            'ano_inicio': self.ano_inicio,
            'mes_fim': self.mes_fim,
	        'ano_fim': self.ano_fim,
            'codigo_orgao': self.codigo_orgao,
            'nome_orgao': self.nome_orgao,
            'codigo_unidade': self.codigo_unidade,
            'formato_cargo_ou_funcao': self.formato_cargo_ou_funcao,
            'cargo_ou_funcao': self.cargo_ou_funcao,
	        'nome_unidade': self.nome_unidade,
            'cargo_ou_funcao_ingles': self.cargo_ou_funcao_ingles,
        }