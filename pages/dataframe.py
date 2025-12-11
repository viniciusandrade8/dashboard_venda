import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso


#  Adicionando Páginas no dashboard do streamlit
st.title("Dataset de Vendas")
#  Coluna de filtro
with st.expander("Colunas"):
    colunas = st.multiselect(
        "Selecione as Colunas",
        list(df.columns),
        list(df.columns)
        )

#  Criando o menu de filtros das colunas
st.sidebar.title("Filtros")
# filtros das categorias
with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect(
        "Selecione as Categorias",
        df["Categoria do Produto"].unique(),
        df["Categoria do Produto"].unique()
        )
#  filtros do preço do produto
with st.sidebar.expander("Preço do Produto"):
    preco = st.slider(
        "Selecione o Preço",
        0, 5000,
        (0, 5000)
        )
#  Filtro da data da compra
with st.sidebar.expander("Data da Compra"):
    data_compra = st.date_input(
        "Selecione a data",
        (df["Data da Compra"].min(),
        df["Data da Compra"].max())
    )


#  criando as query (consultas) dos filtros com as colunas do dataframe
#  Quando é uma coluna do tipo string utilizamos crase invertido `, não precisa fazer isso para as numéricas
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
filtro_dados = df.query(query) #  Realizando o filtro dos registros
filtro_dados = filtro_dados[colunas] #  Filtrando os dados pelas colunas que selecionamos

#  Mostrando a quantidade de linhas e colunas do dataframe
st.markdown(f"A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas")

#  Importando os dados do dataset para essa página do streamlit
st.dataframe(filtro_dados)

#Download CSV
st.markdown("Escreva o nome do arquivo")

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        "",
        label_visibility="collapsed"
    )
    nome_arquivo += '.CSV'
with coluna2:
    st.download_button(
        "Baixar arquivo",
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime="text/csv",
        on_click=mensagem_sucesso
    )
