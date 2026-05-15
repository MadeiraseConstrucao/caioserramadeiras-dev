import streamlit as st

from components.cards import renderizar_card_cliente
from services.search import buscar_dataframe
from utils.helpers import (
    mostrar_sem_busca,
    mostrar_total_resultados,
    mostrar_logo
)

from config.settings import (
    LOGO_NOME_PATH,
)



def pagina_clientes(df_clientes):

    # ==========================================
    # LOGO
    # ==========================================
    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])

    with col_logo_1:

        mostrar_logo(LOGO_NOME_PATH, 250)
    # ==========================================

    
    st.markdown(
        "<div class='section-title'>👥 CONSULTA DE CLIENTES</div>",
        unsafe_allow_html=True
    )

    busca = st.text_input(
        "🔎 Buscar cliente",
        key="busca_cliente",
        placeholder="Digite nome, CNPJ..."
    )

    if not busca:

        mostrar_sem_busca()
        return

    with st.spinner("Pesquisando clientes..."):

        resultado = buscar_dataframe(df_clientes, busca)

        resultado = resultado.head(50)

    mostrar_total_resultados(len(resultado))

    for _, row in resultado.iterrows():

        renderizar_card_cliente(row)
