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
from pages.orientacao_porta import pagina_orientacao_porta

from components.sidebar import renderizar_sidebar

from config.settings import (
    APP_TITLE,
    LOGO_PATH,
    PAGINA_MENU,
    PAGINA_CLIENTES,
    PAGINA_PRODUTOS,
    PAGINA_ORIENTACAO_PORTA,
)






# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=LOGO_PATH,
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

renderizar_sidebar()



# ==========================================
# MENU PRINCIPAL
# ==========================================





# ==========================================
# ROTEAMENTO
# ==========================================

if st.session_state.pagina == PAGINA_MENU:

    pagina_menu()

elif st.session_state.pagina == "clientes":

    pagina_clientes(df_clientes)

elif st.session_state.pagina == "produtos":

    pagina_produtos(df_produtos)

elif st.session_state.pagina == PAGINA_ORIENTACAO_PORTA:

    pagina_orientacao_porta()

