class Pessoa:
    def __init__(self):
        self.nome_completo = None
        self.nome_citacoes = None
        self.nacionalidade = None
        self.pais_nascimento = None
        self.uf_nascimento = None
        self.permissao_divulgacao = None
        self.data_falecimento = None
        self.sigla_pais_nacionalidade = None
        self.sistema_origem = None
        self.data_atualizacao = None
        self.hora_atualizacao = None
        self.numero_identificador = None

    def parse(self, data):
        self.nome_completo = data.get('NOME-COMPLETO')
        self.nome_citacoes = data.get('NOME-EM-CITACOES-BIBLIOGRAFICAS')
        self.nacionalidade = data.get('NACIONALIDADE')
        self.pais_nascimento = data.get('PAIS-DE-NASCIMENTO')
        self.uf_nascimento = data.get('UF-NASCIMENTO')
        self.permissao_divulgacao = data.get('PERMISSAO-DE-DIVULGACAO')
        self.data_falecimento = data.get('DATA-FALECIMENTO')
        self.sigla_pais_nacionalidade = data.get('SIGLA-PAIS-NACIONALIDADE')
        self.sistema_origem = data.get('SISTEMA-ORIGEM-XML')
        self.data_atualizacao = data.get('DATA-ATUALIZACAO')
        self.hora_atualizacao = data.get('HORA-ATUALIZACAO')
        self.numero_identificador = data.get('NUMERO-IDENTIFICADOR')

    def __dict__(self):
        return {
            'nome_completo': self.nome_completo,
            'nome_citacoes': self.nome_citacoes,
            'nacionalidade': self.nacionalidade,
            'pais_nascimento': self.pais_nascimento,
            'uf_nascimento': self.uf_nascimento,
            'permissao_divulgacao': self.permissao_divulgacao,
            'data_falecimento': self.data_falecimento,
            'sigla_pais_nacionalidade': self.sigla_pais_nacionalidade,
            'sistema_origem': self.sistema_origem,
            'data_atualizacao': self.data_atualizacao,
            'hora_atualizacao': self.hora_atualizacao,
            'numero_identificador': self.numero_identificador,
        }
