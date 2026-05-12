import streamlit as st
    )

    st.markdown(
        "<div class='sub-title'>Sistema interno de ferramentas</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # ==========================================
    # CONSULTA PANGEIA
    # ==========================================

    with col1:

        st.markdown("### 🔎 Consulta Pangeia")

        st.markdown(
            "Consulta rápida de clientes e produtos."
        )

        if st.button(
            "ABRIR CONSULTA",
            use_container_width=True,
            key="menu_consulta"
        ):

            st.session_state.pagina = PAGINA_CLIENTES
            st.rerun()

    # ==========================================
    # ORIENTAÇÃO PORTA
    # ==========================================

    with col2:

        st.markdown("### 🚪 Orientação Visual")

        st.markdown(
            "Ferramenta visual para orientação de abertura de portas."
        )

        if st.button(
            "ABRIR ORIENTAÇÃO",
            use_container_width=True,
            key="menu_porta"
        ):

            st.session_state.pagina = PAGINA_ORIENTACAO_PORTA
            st.rerun()

    # ==========================================
    # FUTURO
    # ==========================================

    with col3:

        st.markdown("### 🚚 Entregas")

        st.markdown(
            "Consulta e acompanhamento de entregas."
        )

        st.info("Em desenvolvimento")
