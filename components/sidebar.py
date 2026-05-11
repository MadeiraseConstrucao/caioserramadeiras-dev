import streamlit as st
from utils.helpers import mostrar_logo


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
