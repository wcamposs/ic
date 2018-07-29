class Especializacao:
    def __init__(self):
        self.sequencia_formacao = None
        self.nivel = None
        self.titulo_da_monografia = None
        self.nome_do_orientador = None
        self.codigo_instituicao = None
        self.nome_instituicao = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.status_do_curso = None
        self.ano_de_inicio = None
        self.ano_de_conclusao = None
        self.flag_bolsa = None
        self.codigo_agencia_financiadora = None
        self.nome_agencia = None
        self.carga_horaria = None
        self.titulo_da_monografia_ingles = None
        self.nome_curso_ingles = None

    def parse(self, data):
        self.sequencia_formacao = None
        self.nivel = None
        self.titulo_da_monografia = None
        self.nome_do_orientador = None
        self.codigo_instituicao = None
        self.nome_instituicao = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.status_do_curso = None
        self.ano_de_inicio = None
        self.ano_de_conclusao = None
        self.flag_bolsa = None
        self.codigo_agencia_financiadora = None
        self.nome_agencia = None
        self.carga_horaria = None
        self.titulo_da_monografia_ingles = None
        self.nome_curso_ingles = None

    def __dict__(self):
        return {
            'sequencia_formação': self.sequencia_formacao,
            'nivel': self.nivel,
            'titulo_da_monografia': self.titulo_da_monografia,
            'nome_do_orientador': self.nome_do_orientador,
            'codigo_instituicao': self.codigo_instituicao,
	        'nome_instituicao': self.nome_instituicao,
            'codigo_orgao': self.codigo_orgao,
            'codigo_curso': self.codigo_curso,
            'nome_curso': self.nome_curso,
            'status_do_curso': self.status_do_curso,
            'ano_de_inicio': self.ano_de_inicio,
            'ano_de_conclusao': self.ano_de_conclusao,
            'flag_bolsa': self.flag_bolsa,
            'codigo_agencia_financiadora': self.codigo_agencia_financiadora,
            'nome_agencia': self.nome_agencia,
            'carga_horaria': self.carga_horaria,
            'titulo_da_monografia_ingles': self.titulo_da_monografia_ingles,
            'nome_curso_ingles': self.nome_curso_ingles,
        }