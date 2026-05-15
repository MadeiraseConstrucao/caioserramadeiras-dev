import streamlit as st

from utils.helpers import mostrar_logo
from utils.helpers import imagem_base64

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

logo_base64 = imagem_base64(LOGO_PATH)

def pagina_menu():

    # ==========================================
    # HEADER
    # ==========================================

 st.markdown(
    f"""
    <style>

    .header-container {{
        display:flex;
        align-items:center;
        justify-content:space-between;

        padding:20px 30px;

        border-radius:20px;

        background: rgba(255,255,255,0.03);

        border:1px solid rgba(255,255,255,0.08);

        margin-bottom:30px;
    }}

    .header-left {{
        display:flex;
        align-items:center;
        gap:20px;
    }}

    .header-title h1 {{
        margin:0;
        font-size:30px;
    }}

    .header-title p {{
        margin:0;
        opacity:0.7;
        font-size:15px;
    }}

    .header-right {{
        text-align:right;
    }}

    .version-label {{
        font-size:13px;
        opacity:0.6;
    }}

    .version-number {{
        font-size:20px;
        font-weight:bold;
    }}

    </style>

    <div class="header-container">

        <div class="header-left">

            <img
                src="data:image/png;base64,{logo_base64}"
                width="90"
            >

            <div class="header-title">

                <h1>
                    UTILITÁRIOS MADEIRAS E CONSTRUÇÃO
                </h1>

                <p>
                    Sistema interno de ferramentas
                </p>

            </div>

        </div>

        <div class="header-right">

            <div class="version-label">
                VERSÃO
            </div>

            <div class="version-number">
                v1.0
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True
)
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
