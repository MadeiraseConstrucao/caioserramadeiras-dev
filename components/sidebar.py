import streamlit as st

from utils.helpers import mostrar_logo

from config.settings import (
    LOGO_PATH,
    PAGINA_MENU,
    PAGINA_CLIENTES,
    PAGINA_PRODUTOS,
    PAGINA_ORIENTACAO_PORTA,
    PAGINA_ENTREGAS
)



# ==========================================
# SIDEBAR
# ==========================================

def renderizar_sidebar():

    with st.sidebar:

        mostrar_logo(LOGO_PATH, 150)

        st.markdown("---")

        st.markdown("### 🏠 Menu Principal")

        if st.button(
            "INÍCIO",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_MENU
            st.rerun()

        st.markdown("---")

        # ==========================================
        # CONSULTA PANGEIA
        # ==========================================

        st.markdown("### 🔎 Consulta Pangeia")

        if st.button(
            "👥 Clientes",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_CLIENTES
            st.rerun()

        if st.button(
            "📦 Produtos",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_PRODUTOS
            st.rerun()

        st.markdown("---")

        # ==========================================
        # ORIENTAÇÃO PORTA
        # ==========================================

        st.markdown("### 🚪 Portas")

        if st.button(
            "Orientação Visual",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_ORIENTACAO_PORTA
            st.rerun()

        st.markdown("---")

        # ==========================================
        # ENTREGAS
        # ==========================================

        st.markdown("### 🚚 Entregas")

        if st.button(
            "Consulta Entregas",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_ENTREGAS
            st.rerun()
