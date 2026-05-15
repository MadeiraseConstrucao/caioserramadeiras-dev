import streamlit as st

from utils.helpers import mostrar_logo

from config.settings import (
    LOGO_PATH,
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
    # HEADER
    # ==========================================

    col_logo, col_titulo, col_info, col_home = st.columns([1, 4, 1.2, 1])

    # LOGO
    with col_logo:

        mostrar_logo(LOGO_PATH, 110)

    # TÍTULOS
    with col_titulo:

        st.markdown(
            """
            <div style="padding-top:10px;">
                <div class="main-title">
                    UTILITÁRIOS MADEIRAS E CONSTRUÇÃO
                </div>

                <div class="sub-title">
                    Sistema interno de ferramentas
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # VERSÃO
    with col_info:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding-top:20px;
            ">
                <div style="
                    font-size:14px;
                    opacity:0.7;
                ">
                    VERSÃO
                </div>

                <div style="
                    font-size:18px;
                    font-weight:bold;
                ">
                    v1.0
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # BOTÃO HOME
    with col_home:

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🏠 HOME",
            use_container_width=True
        ):

            st.session_state.pagina = PAGINA_MENU
            st.rerun()

    st.markdown("---")

    # ==========================================
    # CONTEÚDO
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
