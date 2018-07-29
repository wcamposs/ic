class EnderecoProfissional:
    def __init__(self):
        self.codigo_unidade = None
        self.nome_unidade = None
        self.codigo_orgao = None
        self.nome_orgao = None
        self.pais = None
        self.uf = None
        self.logradouro_complemento = None
        self.bairro = None
        self.cidade = None
        self.caixa_postal = None
        self.cep = None
        self.ddd = None
        self.telefone = None
        self.ramal = None
        self.fax = None
        self.home_page = None

    def parse(self, data):
        self.codigo_unidade = data.get('CODIGO-UNIDADE')
        self.nome_unidade = data.get('NOME-UNIDADE')
        self.codigo_orgao = data.get('CODIGO-ORGAO')
        self.pais = data.get('PAIS')
        self.uf = data.get('UF')
        self.logradouro_complemento = data.get('LOGRADOURO-COMPLEMENTO')
        self.bairro = data.get('BAIRRO')
        self.cidade = data.get('CIDADE')
        self.caixa_postal = data.get('CAIXA-POSTAL')
        self.cep = data.get('CEP')
        self.ddd = data.get('DDD')
        self.telefone = data.get('TELEFONE')
        self.ramal = data.get('RAMAL')
        self.fax = data.get('FAX')
        self.home_page = data.get('HOME-PAGE')

    def __dict__(self):
        return {
            'codigo_unidade': self.codigo_orgao,
            'nome_unidade': self.nome_unidade,
            'pais': self.pais,
            'uf': self.uf,
            'logradouro_complemento': self.logradouro_complemento,
            'bairro': self.bairro,
            'cidade': self.cidade,
            'caixa_postal': self.caixa_postal,
            'cep': self.cep,
            'ddd': self.ddd,
            'telefone': self.telefone,
            'ramal': self.ramal,
            'fax': self.fax,
            'home_page': self.home_page,
        }
