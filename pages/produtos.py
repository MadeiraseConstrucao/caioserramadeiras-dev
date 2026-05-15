import streamlit as st

from components.cards import renderizar_card_produto
from services.search import buscar_dataframe
from utils.helpers import (
    mostrar_sem_busca,
    mostrar_total_resultados,
    mostrar_logo
)


# ==========================================
# PÁGINA PRODUTOS
# ==========================================

def pagina_produtos(df_produtos):

    # ==========================================
    # LOGO
    # ==========================================
    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])

    with col_logo_2:

        mostrar_logo(LOGO_NOME_PATH, 250)
    # ==========================================
    
    
    st.markdown(
        "<div class='section-title'>📦 CONSULTA DE PRODUTOS</div>",
        unsafe_allow_html=True
    )

    busca = st.text_input(
        "🔎 Buscar produto",
        key="busca_produto",
        placeholder="Digite descrição, NCM, unidade..."
    )
    

    if not busca:

        mostrar_sem_busca()
        return

    with st.spinner("Pesquisando produtos..."):

        resultado = buscar_dataframe(
            df_produtos,
            busca
        )

        resultado = resultado.head(50)

    mostrar_total_resultados(len(resultado))

    # ==========================================
    # GRID RESPONSIVO
    # ==========================================

    colunas = st.columns(2)

    for i, (_, row) in enumerate(resultado.iterrows()):

        with colunas[i % 2]:

            renderizar_card_produto(row)
