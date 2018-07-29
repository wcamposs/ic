class Mestrado:
    def __init__(self):
        self.sequencia_formacao = None
        self.nivel = None
        self.codigo_instituicao = None
        self.nome_instituicao = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.codigo_area_curso = None
        self.status_do_curso = None
        self.ano_de_inicio = None
        self.ano_de_conclusao = None
        self.flag_bolsa = None
        self.codigo_agencia_financiadora = None
        self.nome_agencia = None
        self.ano_de_obtencao_do_titulo = None
        self.titulo_da_dissertacao_tese = None
        self.nome_completo_do_orientador = None
        self.tipo_mestrado = None
        self.numero_id_orientador = None
        self.codigo_curso_capes = None
        self.titulo_da_dissertacao_tese_ingles = None
        self.nome_curso_ingles = None
        self.nome_do_co_orientador = None
        self.codigo_instituicao_dout = None
        self.nome_instituicao_dout = None
        self.codigo_instituicao_outra_dout = None
        self.nome_instituicao_outra_dout = None
        self.nome_orientador_dout = None

    def parse(self, data):
        self.sequencia_formacao = None
        self.nivel = None
        self.codigo_instituicao = None
        self.nome_instituicao = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.codigo_curso = None
        self.nome_curso = None
        self.codigo_area_curso = None
        self.status_do_curso = None
        self.ano_de_inicio = None
        self.ano_de_conclusao = None
        self.flag_bolsa = None
        self.codigo_agencia_financiadora = None
        self.nome_agencia = None
        self.ano_de_obtencao_do_titulo = None
        self.titulo_da_dissertacao_tese = None
        self.nome_completo_do_orientador = None
        self.tipo_mestrado = None
        self.numero_id_orientador = None
        self.codigo_curso_capes = None
        self.titulo_da_dissertacao_tese_ingles = None
        self.nome_curso_ingles = None
        self.nome_do_co_orientador = None
        self.codigo_instituicao_dout = None
        self.nome_instituicao_dout = None
        self.codigo_instituicao_outra_dout = None
        self.nome_instituicao_outra_dout = None
        self.nome_orientador_dout = None

    def __dict__(self):
        return {
            'sequencia_formacao': self.sequencia_formacao,
            'nivel': self.nivel,
            'codigo_instituicao': self.codigo_instituicao,
            'nome_instituicao': self.nome_instituicao,
            'codigo_orgao': self.codigo_orgao,
	        'nome_orgao': self.nome_orgao,
            'codigo_curso': self.codigo_curso,
            'nome_curso': self.nome_curso,
            'codigo_area_curso': self.codigo_area_curso,
            'status_do_curso': self.status_do_curso,
            'ano_de_inicio': self.ano_de_inicio,
            'ano_de_conclusao': self.ano_de_conclusao,
            'flag_bolsa': self.flag_bolsa,
            'codigo_agencia_financiadora': self.codigo_agencia_financiadora,
            'nome_agencia': self.nome_agencia,
            'ano_de_obtencao_do_titulo': self.ano_de_obtencao_do_titulo,
            'titulo_da_dissertacao_tese': self.titulo_da_dissertacao_tese,
            'nome_completo_do_orientador': self.nome_completo_do_orientador,
            'tipo_mestrado': self.tipo_mestrado,
            'numero_id_orientador': self.numero_id_orientador,
            'codigo_curso_capes': self.codigo_curso_capes,
            'titulo_da_dissertacao_tese_ingles': self.titulo_da_dissertacao_tese_ingles,
            'nome_curso_ingles': self.nome_curso_ingles,
            'nome_do_co_orientador': self.nome_do_co_orientador,
            'codigo_instituicao_dout': self.codigo_instituicao_dout,
            'nome_instituicao_dout': self.nome_instituicao_dout,
            'codigo_instituicao_outra_dout': self.codigo_instituicao_outra_dout,
            'nome_instituicao_outra_dout': self.nome_instituicao_outra_dout,
            'nome_orientador_dout': self.nome_orientador_dout,
        }