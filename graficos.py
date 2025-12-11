import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, def_rec_categoria, df_vendedores


#  RECEITA
#  1 - Gráfico de mapa
grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = "lat",
    lon = "lon",
    scope = "south america",
    size = "Preço",
    template = "seaborn",
    hover_name = "Local da compra",
    hover_data = {"lat": False, "lon": False},
    title = "Receita por Estado" 
)


#  2 - Gráfico da Receita Mensal
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = "Mes",
    y = "Preço",
    markers = True,
    range_y = (0, df_rec_mensal.max()),
    color = "Ano",
    line_dash = "Ano",
    title = "Receita Mensal"
)
#  Titulo para o eixo y
grafico_rec_mensal.update_layout(yaxis_title = "Receita")


#  3 - Gráfico de barras com os estados que tem a maior receita
grafico_rec_estado = px.bar(
    df_rec_estado.head(5),
    x = "Local da compra",
    y = "Preço",
    text_auto = True,
    title = "Top 5 Receitas por Estado"
)


#  4 - Gráfico de barras com o preço total por categoria
grafico_rec_categoria = px.bar(
    def_rec_categoria.head(5),
    text_auto = True,
    title = "Top 5 Categorias com Maior Receita"
)


#  VENDEDORES
#  1 -  Gráfico de barras - Receita por Vendedores
grafico_rec_vendedores = px.bar(
    df_vendedores[["sum"]].sort_values("sum", ascending=False).head(5),
    x = "sum",
    y = df_vendedores[["sum"]].sort_values("sum", ascending=False).head(5).index,
    text_auto = True,
    title = "Top 5 Vendedores por Receita"
)

#  2 - Gráfico de contagem de vendas por vendedores
grafico_vendas_vendedores = px.bar(
    df_vendedores[["count"]].sort_values("count", ascending = False).head(5),
    x = "count",
    y = df_vendedores[["count"]].sort_values("count", ascending = False).head(5).index,
    text_auto = True,
    title = "Top 5 Vendedores por Vendas"
)
