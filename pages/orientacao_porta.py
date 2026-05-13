import streamlit as st

from components.porta_preview import obter_imagem_porta
from services.porta_service import enviar_pedido_porta


# ==========================================
# ORIENTAÇÃO VISUAL DE PORTA
# ==========================================

def pagina_orientacao_porta():

    st.markdown(
        "<div class='section-title'>🚪 ORIENTAÇÃO VISUAL DE PORTA</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    # ======================================
    # FORMULÁRIO
    # ======================================

    with col1:

        numero_pedido = st.text_input(
            "Número do Pedido"
        )

        nome_cliente = st.text_input(
            "Nome Cliente"
        )

        vendedor = st.text_input(
            "Vendedor"
        )

        medidas_porta = st.text_input(
            "Medidas Porta"
        )

        largura_batente = st.text_input(
            "Largura Batente"
        )

        lado_abertura = st.selectbox(
            "Lado Abertura",
            [
                "DIREITA",
                "ESQUERDA"
            ]
        )

        abre_para = st.selectbox(
            "Abre Para",
            [
                "FORA DO AMBIENTE",
                "DENTRO DO AMBIENTE"
            ]
        )

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
