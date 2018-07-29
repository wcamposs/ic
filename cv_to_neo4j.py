# Importando módulos nativos do Python
import json
import os

# Importando módulos de terceiros
from neo4jrestclient.client import GraphDatabase
import xmltodict

# Importando módulos locais
from cv import (
    AreaAtuacao,
    EnderecoProfissional,
    Instituicao,
    Pessoa,
    ResumoCV,
    FormacaoAcademicaTitulacao,
    Graduacao,
    Idioma,
    Especializacao,
    Mestrado,
    PalavrasChave,
    AreasDoConhecimento,
    Doutorado,
    Vinculo,
    DirecaoEAdministracao,
    PesquisaEDesenvolvimento,
    LinhaDePesquisa,
    Ensino,
    Disciplina,
    ServicoTecnicoEspecializado,

)


# Constantes
NEO4J_URI = 'http://localhost:7474'
NEO4J_USERNAME = 'neo4j'
NEO4J_PASSWORD = 'phantom2013'

# Conexão com o Neo4j
db = GraphDatabase(
    NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
)

label_area_atuacao = db.labels.create('AreaAtuacao')
label_ends_profs = db.labels.create('EnderecosProfissionais')
label_formacao_academica_titulacao = db.labels.create('FormacaoAcademicaTitulacao')
label_idioma = db.labels.create('Idioma')
label_instituicao = db.labels.create('Instituicao')
label_resumos_cv = db.labels.create('ResumosCV')
label_pessoas = db.labels.create('Pessoas')
label_graduacao = db.labels.create('Graduacao')
label_especializacao = db.labels.create('Especializacao')
label_mestrado = db.labels.create('Mestrado')
label_palavras_chave = db.labels.create('PalavrasChave')
label_areas_do_conhecimento = db.labels.create('AreasDoConhecimento')
label_doutorado = db.labels.create('Doutorado')
label_vinculo = db.labels.create('Vinculo')
label_direcao_e_administracao = db.labels.create('DirecaoEAdministracao')
label_pesquisa_e_desenvolvimento = db.labels.create('PesquisaEDesenvolvimento')
label_linha_de_pesquisa = db.labels.create('LinhaDePesquisa')
label_ensino = db.labels.create('Ensino')
label_disciplina = db.labels.create('Disciplina')
label_servico_tecnico_especializado = db.labels.create('ServicoTecnicoEspecializado')

_instituicoes = {}


# Define a pasta onde estao os arquivos
for filename in os.listdir('curriculos'):

    filepath = '/'.join(['curriculos', filename])

    # Abre o  arquivo para leitura
    with open (filepath, 'r', encoding='ISO-8859-1') as file:

        # Ler o conteúdo do arquivo
        content = file.read()

        # Converte o conteúdo XML para dicionário
        content = xmltodict.parse(content)

        # Converte o dicionário para JSON string e remove os @ das chaves que o xmltodict gerou após a conversão
        content = json.dumps(content).replace('@', '').replace('_', '')

        # Retorna de JSON string para dicionário
        content = json.loads(content)

        # Adicionando instituicoes


        # Criando o objeto pessoa
        pessoa_obj = Pessoa()
        pessoa_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS'])
        pessoa = db.nodes.create(**pessoa_obj.__dict__())
        label_pessoas.add(pessoa)

        #Adicionando o resumo curricular 
        if 'RESUMO-CV' in content['CURRICULO-VITAE']['DADOS-GERAIS']:
            resumo_obj = ResumoCV()
            resumo_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['RESUMO-CV'])
            resumo_cv = db.nodes.create(**resumo_obj.__dict__())
            label_resumos_cv.add(resumo_cv)
            pessoa.relationships.create('Possui', resumo_cv)

        #Adicionando Endereço Profissional
        if 'ENDERECO-PROFISSIONAL' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ENDERECO']:
            end_prof_obj = EnderecoProfissional()
            end_prof_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ENDERECO']['ENDERECO-PROFISSIONAL'])
            end_prof = db.nodes.create(**end_prof_obj.__dict__())
            label_ends_profs.add(end_prof)
            pessoa.relationships.create('Possui', end_prof)

        #Adicionando área de atuação
        if 'AREA-DE-ATUACAO' in content.get('AREAS-DE-ATUACAO', {}):
            area_atuacao_obj = AreaAtuacao()
            area_atuacao_obj.parse(content['AREAS-DE-ATUACAO']['AREA-DE-ATUACAO'])
            area_atuacao = db.nodes.create(**area_atuacao_obj.__dict__())
            label_area_atuacao.add(area_atuacao)
            pessoa.relationships.create('Possui', area_atuacao)

        #Adicionando idiomas
        if 'IDIOMAS' in content['CURRICULO-VITAE']['DADOS-GERAIS']:
            idioma_obj = Idioma()
            idioma_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['IDIOMAS']['IDIOMA'])
            idioma = db.nodes.create(**idioma_obj.__dict__())
            label_idioma.add(idioma)
            pessoa.relationships.create('Possui', idioma)

        #Adicionando formações academicas em geral
        if 'FORMACAO-ACADEMICA-TITULACAO' in content['CURRICULO-VITAE']['DADOS-GERAIS']:
            formacao_academica_titulacao_obj = FormacaoAcademicaTitulacao()
            formacao_academica_titulacao_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO'])
            formacao_academica_titulacao = db.nodes.create(**formacao_academica_titulacao_obj.__dict__())
            label_formacao_academica_titulacao.add(formacao_academica_titulacao)
            pessoa.relationships.create('Possui', formacao_academica_titulacao)

            #Adicionando Graduação (caso haja)
            if 'GRADUACAO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']:
                graduacao_obj = Graduacao()
                graduacao_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['GRADUACAO'])
                graduacao = db.nodes.create(**graduacao_obj.__dict__())
                label_graduacao.add(graduacao)
                pessoa.relationships.create('Possui', graduacao)
            
            #Adicionando Especialização (caso haja)
            if 'ESPECIALIZACAO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']:
                especializacao_obj = Especializacao()
                especializacao_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['ESPECIALIZACAO'])
                especializacao = db.nodes.create(**especializacao_obj.__dict__())
                label_especializacao.add(especializacao)
                pessoa.relationships.create('Possui', especializacao)

            #Adicionando Mestrado (caso haja)
            if 'MESTRADO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']:
                mestrado_obj = Mestrado()
                mestrado_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['MESTRADO'])
                mestrado = db.nodes.create(**mestrado_obj.__dict__())
                label_mestrado.add(mestrado)
                pessoa.relationships.create('Possui', mestrado)

                #Adicionando as palavras chave ao mestrado
                if 'PALAVRAS-CHAVE' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['MESTRADO']:
                    palavras_chave_obj = PalavrasChave()
                    palavras_chave_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['MESTRADO']['PALAVRAS-CHAVE'])
                    palavras_chave = db.nodes.create(**palavras_chave_obj.__dict__())
                    label_palavras_chave.add(palavras_chave)
                    pessoa.relationships.create('Possui', palavras_chave)
                
                #Adicionando áreas do conhecimento ao mestrado
                if 'AREAS-DO-CONHECIMENTO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['MESTRADO']:
                    areas_do_conhecimento_obj = PalavrasChave()
                    areas_do_conhecimento_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['MESTRADO']['AREAS-DO-CONHECIMENTO'])
                    areas_do_conhecimento = db.nodes.create(**areas_do_conhecimento_obj.__dict__())
                    label_areas_do_conhecimento.add(areas_do_conhecimento)
                    pessoa.relationships.create('Possui', areas_do_conhecimento)

            #Adicionando Doutorado (caso haja)
            if 'DOUTORADO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']:
                doutorado_obj = Doutorado()
                doutorado_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['DOUTORADO'])
                doutorado = db.nodes.create(**doutorado_obj.__dict__())
                label_doutorado.add(doutorado)
                pessoa.relationships.create('Possui', doutorado)

                #Adicionando palavras chave ao doutorado
                if 'PALAVRAS-CHAVE' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['DOUTORADO']:
                    palavras_chave_obj = PalavrasChave()
                    palavras_chave_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['DOUTORADO']['PALAVRAS-CHAVE'])
                    palavras_chave = db.nodes.create(**palavras_chave_obj.__dict__())
                    label_palavras_chave.add(palavras_chave)
                    pessoa.relationships.create('Possui', palavras_chave)
                
                #Adicionando áreas do conhecimento ao doutorado
                if 'AREAS-DO-CONHECIMENTO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['DOUTORADO']:
                    areas_do_conhecimento_obj = PalavrasChave()
                    areas_do_conhecimento_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['FORMACAO-ACADEMICA-TITULACAO']['DOUTORADO']['AREAS-DO-CONHECIMENTO'])
                    areas_do_conhecimento = db.nodes.create(**areas_do_conhecimento_obj.__dict__())
                    label_areas_do_conhecimento.add(areas_do_conhecimento)
                    pessoa.relationships.create('Possui', areas_do_conhecimento)

        #Adicionando vinculos (caso hajam)
        if 'VINCULOS' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']:
            vinculo_obj = Vinculo()
            vinculo_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['VINCULOS'])
            vinculo = db.nodes.create(**vinculo_obj.__dict__())
            label_vinculo.add(vinculo)
            pessoa.relationships.create('Possui ou possuiu vinculo', vinculo)

        #Adicionando atividades de direcao e administracao (caso hajam)
        if 'ATIVIDADES-DE-DIRECAO-E-ADMINISTRACAO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']:
            direcao_e_administracao_obj = DirecaoEAdministracao()
            direcao_e_administracao_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-DIRECAO-E-ADMINISTRACAO']['DIRECAO-E-ADMINISTRACAO'])
            direcao_e_administracao = db.nodes.create(**direcao_e_administracao_obj.__dict__())
            label_direcao_e_administracao.add(direcao_e_administracao)
            pessoa.relationships.create('Possui ou possuiu', direcao_e_administracao)

        #Adicinando atividades de pesquisa e desenvolvimento (caso hajam)
        if 'ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']:
            pesquisa_e_desenvolvimento_obj = PesquisaEDesenvolvimento()
            pesquisa_e_desenvolvimento_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO']['PESQUISA-E-DESENVOLVIMENTO'])
            pesquisa_e_desenvolvimento = db.nodes.create(**pesquisa_e_desenvolvimento_obj.__dict__())
            label_pesquisa_e_desenvolvimento.add(pesquisa_e_desenvolvimento)

            #Adicionando linha de pesquisa as atividades de pesquisa e desenvolvimento
            if 'LINHA-DE-PESQUISA' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO']['PESQUISA-E-DESENVOLVIMENTO']:
                linha_de_pesquisa_obj = LinhaDePesquisa()
                linha_de_pesquisa_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-PESQUISA-E-DESENVOLVIMENTO']['PESQUISA-E-DESENVOLVIMENTO']['LINHA-DE-PESQUISA'])
                linha_de_pesquisa = db.nodes.create(**linha_de_pesquisa_obj.__dict__())
                label_linha_de_pesquisa.add(linha_de_pesquisa)
                pessoa.relationships.create('Fez ou faz parte de', linha_de_pesquisa)

        #Adicionando atividades de ensino (caso hajam)
        if 'ATIVIDADES-DE-ENSINO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']:
            ensino_obj = Ensino()
            ensino_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-ENSINO']['ENSINO'])
            ensino = db.nodes.create(**ensino_obj.__dict__())
            label_ensino.add(ensino)
            pessoa.relationships.create('Ensina ou ensinou', ensino)

            #Adicionando disciplina as atividades de ensino
            if 'DISCIPLINA' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-ENSINO']['ENSINO']:
                disciplina_obj = Disciplina()
                disciplina_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-ENSINO']['ENSINO']['DISCIPLINA'])
                disciplina = db.nodes.create(**disciplina_obj.__dict__())
                label_disciplina.add(disciplina)
                pessoa.relationships.create('Ensina ou ensinou a disciplina', disciplina)

        #Adicionando atividades de serviço técnico (caso haja)
        if 'ATIVIDADES-DE-SERVICO-TECNICO-ESPECIALIZADO' in content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']:
            servico_tecnico_especializado_obj = ServicoTecnicoEspecializado()
            servico_tecnico_especializado_obj.parse(content['CURRICULO-VITAE']['DADOS-GERAIS']['ATUACOES-PROFISSIONAIS']['ATUACAO-PROFISSIONAL']['ATIVIDADES-DE-SERVICO-TECNICO-ESPECIALIZADO']['SERVICO-TECNICO-ESPECIALIZADO'])
            servico_tecnico_especializado = db.nodes.create(**servico_tecnico_especializado_obj.__dict__())
            label_servico_tecnico_especializado.add(servico_tecnico_especializado)
            pessoa.relationships.create('Atua ou atuou', servico_tecnico_especializado)