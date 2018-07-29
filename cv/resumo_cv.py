class ResumoCV:
    def __init__(self):
        self.texto_resumo_cv_rh_en = None
        self.texto_resumo_cv_rh = None
        self.data = None

    def parse(self, data):
        self.texto_resumo_cv_rh = data.get('TEXTO-RESUMO-CV-RH')
        self.texto_resumo_cv_rh_en = data.get('TEXTO-RESUMO-CV-RH-EN')

    def __dict__(self):
        return {
            'texto_resumo_cv_rh': self.texto_resumo_cv_rh,
            'texto_resumo_cv_rh_en': self.texto_resumo_cv_rh_en,
        }
