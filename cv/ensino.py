class Ensino:
    def __init__(self):
        self.sequencia_funcao_atividade = None
        self.flag_periodo = None
        self.tipo_ensino = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.nome_curso_ingles = None

    def parse(self, data):
        self.sequencia_funcao_atividade = None
        self.flag_periodo = None
        self.tipo_ensino = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.nome_curso_ingles = None

    def __dict__(self):
        return {
            'sequencia_funcao_atividade': self.sequencia_funcao_atividade,
            'flag_periodo': self.flag_periodo,
            'tipo_ensino': self.tipo_ensino,
            'mes_inicio': self.mes_inicio,
            'ano_inicio': self.ano_inicio,
	        'mes_fim': self.mes_fim,
            'ano_fim': self.ano_fim,
            'codigo_orgao': self.codigo_orgao,
            'nome_orgao': self.nome_orgao,
            'codigo_curso': self.codigo_curso,
            'nome_curso': self.nome_curso,
	        'nome_curso_ingles': self.nome_curso_ingles,
        }