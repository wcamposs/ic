#importando as classes
from .area_atuacao import AreaAtuacao
from .endereco_profissional import EnderecoProfissional
from .instituicao import Instituicao
from .pessoa import Pessoa
from .resumo_cv import ResumoCV
from .area_atuacao import AreaAtuacao
from .idioma import Idioma
from .formacao_academica_titulacao import FormacaoAcademicaTitulacao
from .graduacao import Graduacao
from .especializacao import Especializacao
from .mestrado import Mestrado
from .palavras_chave import PalavrasChave
from .areas_do_conhecimento import AreasDoConhecimento
from .doutorado import Doutorado
from .vinculo import Vinculo
from .direcao_e_administracao import DirecaoEAdministracao
from .pesquisa_e_desenvolvimento import PesquisaEDesenvolvimento
from .linha_de_pesquisa import LinhaDePesquisa
from .ensino import Ensino
from .disciplina import Disciplina
from .servico_tecnico_especializado import ServicoTecnicoEspecializado


#criando uma lista para que o conteúdo das classes sejam importados como atributos ao criar o node
__all__ = [
    'AreaAtuacao',
    'EnderecoProfissional',
    'Instituicao',
    'Pessoa',
    'ResumoCV',
    'AreaAtuacao',
    'Idioma',
    'FormacaoAcademicaTitulacao',
    'Graduacao',
    'Especializacao',
    'Mestrado',
    'PalavrasChave',
    'AreasDoConhecimento',
    'Doutorado',
    'Vinculo',
    'DirecaoEAdministracao',
    'PesquisaEDesenvolvimento',
    'LinhaDePesquisa',
    'Ensino',
    'Disciplina',
    'ServicoTecnicoEspecializado',
]
