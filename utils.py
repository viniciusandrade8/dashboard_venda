from dataset import df
import pandas as pd
import streamlit as st
import time


def format_number(value, prefix = ""):
    for unit in ["", "mil"]:
        if value < 1000:
            return f"{prefix} {value:.2f} {unit}"
        value /= 1000
    return f"{prefix} {value:.2f} milhões"



#  Para cada insight vamos primeiro criar uma tabela especifica dentro de utils e depois importamos para o arquivos dos gráficos


#  1 - Criando um DataFrame da receita por Estado
#  Agrupando pelo local da compra e pelo somatório do preço
df_rec_estado = df.groupby("Local da compra")[["Preço"]].sum()
#  Eliminando as duplicatas na coluna local da compra
df_rec_estado = df.drop_duplicates(subset="Local da compra")[["Local da compra", "lat", "lon"]].merge(df_rec_estado, left_on="Local da compra", right_index=True).sort_values("Preço", ascending=False)


#  2 - Dataframe Receita Mensal
#  Alterando o índice para a coluna data da compra, ordenamos por mês e somamos a coluna de preço
df_rec_mensal = df.set_index("Data da Compra").groupby(pd.Grouper(freq="M"))["Preço"].sum().reset_index()
#  Criando a coluna ano para o df, informação retirada da coluna Data da compra pegando só o ano
df_rec_mensal["Ano"] = df_rec_mensal["Data da Compra"].dt.year
#  Criando a coluna mês para o df, informação retirada da coluna Data da compra pegando só o nome do mês
df_rec_mensal["Mes"] = df_rec_mensal["Data da Compra"].dt.month_name()


#  3 = Dataframe Receita por Categoria
def_rec_categoria = df.groupby("Categoria do Produto")[["Preço"]].sum().sort_values("Preço", ascending=False)


#  4 - Dataframe Vendedores
df_vendedores = pd.DataFrame(df.groupby("Vendedor")["Preço"].agg(["sum", "count"]))


#  Download
#  Função para converter arquivo CSV
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

#  Mensagem de conclusão de arquivo baixado.
def mensagem_sucesso():
    success = st.success(
        "Arquivo Baixado com Sucesso",
        icon="🚀"
        )
    time.sleep(5)
    success.empty()

