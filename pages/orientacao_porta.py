import streamlit as st
        vendo_de = st.selectbox(
            "Vendo De",
            [
                "DENTRO",
                "FORA"
            ]
        )

        upload_pdf = st.file_uploader(
            "Orçamento PDF",
            type=["pdf"],
            accept_multiple_files=True
        )

    # ======================================
    # PREVIEW
    # ======================================

    with col2:

        caminho_imagem = obter_imagem_porta(
            lado_abertura,
            abre_para,
            vendo_de
        )

        if caminho_imagem:

            st.image(
                caminho_imagem,
                use_container_width=True
            )

    st.markdown("---")

    # ======================================
    # ENVIAR
    # ======================================

    if st.button(
        "GERAR PEDIDO",
        use_container_width=True
    ):

        dados = {
            "numero_pedido": numero_pedido,
            "nome_cliente": nome_cliente,
            "vendedor": vendedor,
            "medidas_porta": medidas_porta,
            "largura_batente": largura_batente,
            "lado_abertura": lado_abertura,
            "abre_para": abre_para,
            "vendo_de": vendo_de
        }

        with st.spinner("Gerando pedido..."):

            resposta = enviar_pedido_porta(dados)

        if resposta.get("success"):

            st.success("Pedido enviado com sucesso")

        else:

            st.error("Erro ao gerar pedido")
