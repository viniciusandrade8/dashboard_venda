import streamlit as st
import plotly.express as px
from pages.dataset import df
from pages.utils import format_number
from pages.graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores


st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide"
)


st.set_page_config(layout="wide")  #  Definindo a tela para inteira
st.title("Dashboard de Vendas")  #  Titulo do dashboard


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  FILTROS
st.sidebar.title("Filtro de Vendedores")
#  Multiseleção para o filtro de vendedores
filtro_vendedor = st.sidebar.multiselect(
    "Vendedores",
    df["Vendedor"].unique(),
)

if filtro_vendedor:
    df = df[df["Vendedor"].isin(filtro_vendedor)]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Criando abas
aba1, aba2, aba3 = st.tabs(["Dataset", "Receita", "Vendedores"])

#  DATASET
#  Trazendo o DataFrame para a aba1 no dashboard
with aba1:
    st.dataframe(df)

#  RECEITAS
#  Criando as métricas na aba2
with aba2:
    #  Dividindo a aba em duas colunas para as métricas
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        #  Somatório da coluna Preço
        st.metric("Receita Total", format_number(df["Preço"].sum(), "R$"))
        st.plotly_chart(grafico_map_estado, use_container_width = True)
        st.plotly_chart(grafico_rec_estado, use_container_width = True)
    with coluna2:
        #  Quantidade total das vendas
        st.metric("Quantidade de Vendas", format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width = True)
        st.plotly_chart(grafico_rec_categoria, use_container_width = True)

#  RECEITAS
#  Criando as métrica na aba3
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~