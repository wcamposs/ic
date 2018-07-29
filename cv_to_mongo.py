import json
import os #biblioteca nativa com funcoes relacionadas ao sistema operacional (input / output)
import xmltodict

from pymongo import MongoClient #biblioteca para comunicar-se com o mongodb

# Instancia o MongoDB e conecta no banco de dados
mongodb =  MongoClient('mongodb://localhost:27017')

# Selecionando a coleção que irá armazenar os currículos
mongodb = mongodb['CI']

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
        content = json.dumps(content).replace('@', '')
        
        # Retorna de JSON string para dicionário
        content = json.loads(content)

    # Insere o dicionário no MongoDB
    mongodb['curriculos'].insert(content)