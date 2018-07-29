class Vinculo:
    def __init__(self):
        self.sequencia_historico = None
        self.tipo_de_vinculo = None
        self.enquadramento_funcional = None
        self.carga_horaria_semanal = None
        self.flag_dedicacao_exclusiva = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.outras_informacoes = None
        self.flag_vinculo_empregaticio = None
        self.outro_vinculo_informado = None
        self.outro_enquadramento_funcional_informado = None
        self.outro_enquadramento_funcional_informado_ingles = None
        self.outras_informacoes_ingles = None

    def parse(self, data):
        self.sequencia_historico = None
        self.tipo_de_vinculo = None
        self.enquadramento_funcional = None
        self.carga_horaria_semanal = None
        self.flag_dedicacao_exclusiva = None
        self.mes_inicio = None
        self.ano_inicio = None
        self.mes_fim = None
        self.ano_fim = None
        self.outras_informacoes = None
        self.flag_vinculo_empregaticio = None
        self.outro_vinculo_informado = None
        self.outro_enquadramento_funcional_informado = None
        self.outro_enquadramento_funcional_informado_ingles = None
        self.outras_informacoes_ingles = None

    def __dict__(self):
        return {
            'sequencia_historico': self.sequencia_historico,
            'tipo_de_vinculo': self.tipo_de_vinculo,
            'enquadramento_funcional': self.enquadramento_funcional,
            'carga_horaria_semanal': self.carga_horaria_semanal,
            'flag_dedicacao_exclusiva': self.flag_dedicacao_exclusiva,
	        'mes_inicio': self.mes_inicio,
            'ano_inicio': self.ano_inicio,
            'mes_fim': self.mes_fim,
            'ano_fim': self.ano_fim,
            'outras_informacoes': self.outras_informacoes,
            'flag_vinculo_empregaticio': self.flag_vinculo_empregaticio,
            'outro_vinculo_informado': self.outro_vinculo_informado,
            'outro_enquadramento_funcional_informado': self.outro_enquadramento_funcional_informado,
            'outro_enquadramento_funcional_informado_ingles': self.outro_enquadramento_funcional_informado_ingles,
            'outras_informacoes_ingles': self.outras_informacoes_ingles,
        }