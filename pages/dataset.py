import json
import pandas as pd

#  Carregando o arquivo JSON
file = open("dados/vendas.json")
data = json.load(file)

#  print(data)

#  Criando um DataFrame baseando em dicionário
df = pd.DataFrame.from_dict(data)

#  Mostrando o DataFrame
#  print(df)

#  Convertendo a coluna de data da compra para formato de Data
df["Data da Compra"] = pd.to_datetime(df["Data da Compra"], format="%d/%m/%Y")

file.close()
