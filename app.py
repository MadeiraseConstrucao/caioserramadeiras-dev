# area de desenvolvimento do site de utilidades da madeiras e construção


# ==========================================
# IMPORTS
# ==========================================

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import re
import base64
import unicodedata

from utils.helpers import (
    tratar,
    limpar_texto,
    formatar_preco,
    mostrar_sem_busca,
    mostrar_total_resultados,
    mostrar_logo
)

from services.loaders import (
    carregar_clientes,
    carregar_produtos
)

from components.cards import (
    renderizar_card_cliente,
    renderizar_card_produto
)

from pages.clientes import pagina_clientes
from pages.produtos import pagina_produtos


# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Consulta Pangeia",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS GLOBAL
# ==========================================

def carregar_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

carregar_css()




# ==========================================
# DATAFRAMES
# ==========================================

with st.spinner("Carregando sistema..."):

    df_clientes = carregar_clientes()
    df_produtos = carregar_produtos()



# ==========================================
# SESSION STATE
# ==========================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"

if "busca_cliente" not in st.session_state:
    st.session_state.busca_cliente = ""

if "busca_produto" not in st.session_state:
    st.session_state.busca_produto = ""



# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    mostrar_logo("logo.png", 150)

    st.markdown("---")

    if st.button("🏠 Menu Inicial", use_container_width=True):

        st.session_state.pagina = "menu"
        st.rerun()

    if st.button("👥 Clientes", use_container_width=True):

        st.session_state.pagina = "clientes"
        st.rerun()

    if st.button("📦 Produtos", use_container_width=True):

        st.session_state.pagina = "produtos"
        st.rerun()

# ==========================================
# MENU PRINCIPAL
# ==========================================

def pagina_menu():

    st.markdown(
        "<div class='main-title'>CONSULTA PANGEIA</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Sistema de consulta interna</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # ==========================================
    # CLIENTES
    # ==========================================

    with col1:

        st.markdown("### 👥 Clientes")

        st.markdown(
            "Consulta rápida por Nome, CNPJ e CPF."
        )

        if st.button(
            "ABRIR CONSULTA CLIENTES",
            use_container_width=True
        ):

            st.session_state.pagina = "clientes"
            st.rerun()

    # ==========================================
    # PRODUTOS
    # ==========================================

    with col2:

        st.markdown("### 📦 Produtos")

        st.markdown(
            "Consulta de produtos por Descrição, NCM, Unidade e Preço."
        )

        if st.button(
            "ABRIR CONSULTA PRODUTOS",
            use_container_width=True
        ):

            st.session_state.pagina = "produtos"
            st.rerun()





# ==========================================
# ROTEAMENTO
# ==========================================

if st.session_state.pagina == "menu":

    pagina_menu()

elif st.session_state.pagina == "clientes":

    pagina_clientes()

elif st.session_state.pagina == "produtos":

    pagina_produtos()

