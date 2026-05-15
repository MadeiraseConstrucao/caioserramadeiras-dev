import streamlit as st

from utils.helpers import mostrar_logo

from config.settings import (
    LOGO_PATH,
    LOGO_NOME_PATH,
    PAGINA_MENU,
    PAGINA_CLIENTES,
    PAGINA_PRODUTOS,
    PAGINA_ORIENTACAO_PORTA
)


# ==========================================
# MENU PRINCIPAL
# ==========================================

def pagina_menu():

    # ==========================================
    # LOGO
    # ==========================================

    col_logo_1, col_logo_2, col_logo_3 = st.columns([1, 1, 1])

    with col_logo_2:

        mostrar_logo(LOGO_NOME_PATH, 250)

    # ==========================================
    # TÍTULOS
    # ==========================================

    st.markdown(
        "<div class='main-title'>UTILITÁRIOS</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Sistema interno de ferramentas</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # CARDS
    # ==========================================

    col1, col2, col3 = st.columns(3)

    # ==========================================
    # CONSULTA PANGEIA
    # ==========================================

    with col1:

        st.markdown(
            """
            <div class='menu-card'>
                <h3>🔎 CONSULTA PANGEIA</h3>
                <p>Consulta rápida de clientes e produtos.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "CLIENTES",
            use_container_width=True,
            key="menu_clientes"
        ):

            st.session_state.pagina = PAGINA_CLIENTES
            st.rerun()

        if st.button(
            "PRODUTOS",
            use_container_width=True,
            key="menu_produtos"
        ):

            st.session_state.pagina = PAGINA_PRODUTOS
            st.rerun()

    # ==========================================
    # ORIENTAÇÃO PORTA
    # ==========================================

    with col2:

        st.markdown(
            """
            <div class='menu-card'>
                <h3>🚪 PORTAS</h3>
                <p>Ferramentas relacionadas a portas.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "ORIENTAÇÃO VISUAL",
            use_container_width=True,
            key="menu_porta"
        ):

            st.session_state.pagina = PAGINA_ORIENTACAO_PORTA
            st.rerun()

    # ==========================================
    # ENTREGAS
    # ==========================================

    with col3:

        st.markdown(
            """
            <div class='menu-card'>
                <h3>🚚 ENTREGAS</h3>
                <p>Ferramentas de logística e entrega...</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='badge-dev'>
                EM DESENVOLVIMENTO...
            </div>
            """,
            unsafe_allow_html=True
        )
