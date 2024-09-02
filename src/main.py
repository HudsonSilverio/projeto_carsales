import pandas  as pd
import sqlite3
from datetime import datetime


# Definindo o caminho para o arquivo da coleta
df = pd.read_json('../data/data.jsonl', lines=True)


# Colocando o pandas para mostrar todas as colunas
pd.options.display.max_columns= None


#add colunas de identificação básica
df['_source'] = 'https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes-em-minas-gerais/carro-a-venda'
#add colunas de identificacao basica
df['_data_coleta'] = datetime.now()



# conectar a um banco de dados
conn = sqlite3.connect('../data/quates.db')


#salvar o DataFrame no banco de Dados SQLite
df.to_sql('mercadolivre_carsales', conn, if_exists='replace', index=False)


# fechando a conexao com o banco de dados
conn.close()

print(df.head())