class Graduacao:
    def __init__(self):
        self.sequencia_formacao = None
        self.nivel = None
        self.titulo_do_trabalho_de_conclusao_de_curso = None
        self.nome_do_orientador = None
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
        self.numero_id_orientador = None
        self.codigo_curso_capes = None
        self.titulo_do_trabalho_de_conclusao_de_curso_ingles = None
        self.nome_curso_ingles = None
        self.formacao_academica_titulacao = None
        self.tipo_graduacao = None
        self.codigo_instituicao_grad = None
        self.nome_instituicao_grad = None
        self.codigo_instituicao_outra_grad = None
        self.nome_instituicao_outra_grad = None
        self.nome_orientador_grad = None

    def parse(self, data):
        self.sequencia_formacao = data.get('SEQUENCIA-FORMACAO')
        self.nivel = data.get('NIVEL')
        self.titulo_do_trabalho_de_conclusao_de_curso = data.get('TITULO-DO-TRABALHO-DE-CONCLUSAO-DE-CURSO')
        self.nome_do_orientador = data.get('NOME-DO-ORIENTADOR')
        self.codigo_instituicao = data.get('CODIGO-INSTITUICAO')
        self.nome_instituicao = data.get('NOME-INSTITUICAO')
        self.codigo_orgao = data.get('CODIGO-ORGAO')
        self.nome_orgao = data.get('NOME-ORGAO')
        self.codigo_curso = data.get('CODIGO-CURSO')
        self.nome_curso = data.get('NOME-CURSO')
        self.codigo_area_curso = data.get('CODIGO-AREA-CURSO')
        self.status_do_curso = data.get('STATUS-DO-CURSO')
        self.ano_de_inicio = data.get('ANO-DE-INICIO')
        self.ano_de_conclusao = data.get('ANO-DE-CONCLUSAO')
        self.flag_bolsa = data.get('FLAG-BOLSA')
        self.codigo_agencia_financiadora = data.get('CODIGO-AGENCIA-FINANCIADORA')
        self.nome_agencia = data.get('NOME-AGENCIA')
        self.numero_id_orientador = data.get('NUMERO-ID-ORIENTADOR')
        self.codigo_curso_capes = data.get('CODIGO-CURSO-CAPES')
        self.titulo_do_trabalho_de_conclusao_de_curso_ingles = data.get('TITULO-DO-TRABALHO-DE-CONCLUSAO-DE-CURSO-INGLES')
        self.nome_curso_ingles = data.get('NOME-CURSO-INGLES')
        self.formacao_academica_titulacao = data.get('FORMACAO-ACADEMICA-TITULACAO')
        self.tipo_graduacao = data.get('TIPO-GRADUACAO')
        self.codigo_instituicao_grad = data.get('CODIGO-INSTITUICAO-GRAD')
        self.nome_instituicao_grad = data.get('NOME-INSTITUICAO-GRAD')
        self.codigo_instituicao_outra_grad = data.get('CODIGO-INSTITUICAO-OUTRA-GRAD')
        self.nome_instituicao_outra_grad = data.get('NOME-INSTITUICAO-OUTRA-GRAD')
        self.nome_orientador_grad = data.get('NOME-ORIENTADOR-GRAD')

    def __dict__(self):
        return {
            'sequencia_formacao': self.sequencia_formacao,
            'nivel': self.nivel,
            'titulo_do_trabalho_de_conclusao_de_curso': self.titulo_do_trabalho_de_conclusao_de_curso,
            'nome_do_orientador': self.nome_do_orientador,
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
            'numero_id_orientador': self.numero_id_orientador,
            'codigo_curso_capes': self.codigo_curso_capes,
            'titulo_do_trabalho_de_conclusao_de_curso_ingles': self.titulo_do_trabalho_de_conclusao_de_curso_ingles,
            'nome_curso_ingles': self.nome_curso_ingles,
            'formacao_academica_titulacao': self.formacao_academica_titulacao,
            'tipo_graduacao': self.tipo_graduacao,
            'codigo_instituicao_grad': self.codigo_instituicao_grad,
            'nome_instituicao_grad': self.nome_instituicao_grad,
            'codigo_instituicao_outra_grad': self.codigo_instituicao_outra_grad,
            'nome_orientador_grad': self.nome_orientador_grad,
        }
