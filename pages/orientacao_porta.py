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
            "NÚMERO DO PEDIDO:"
        )

        vendedor = st.text_input(
            "NOME DO CLIENTE:"
        )

        nome_cliente = st.selectbox(
            "VENDEDOR(A):",
            [
                "CAIO",
                "FIAMMA",         
                "LAISA",
                "LUCIANA",
                "PRISCYLA",
                "THALIA"
            ]
        )

        medidas_porta = st.text_input(
            "MEDIDAS DA PORTA:"
        )

        largura_batente = st.text_input(
            "LARGURA DO BATENTE:"
        )

        vendo_de = st.selectbox(
            "VENDO DE:",
            [
                "DENTRO",
                "FORA"
            ]
        )

        abre_para = st.selectbox(
            "ABRE PARA:",
            [
                "FORA DO AMBIENTE",
                "DENTRO DO AMBIENTE"
            ]
        )
        
        lado_abertura = st.selectbox(
            "LADO DE ABERTURA:",
            [
                "DIREITA",
                "ESQUERDA"
            ]
        )

        upload_pdf = st.file_uploader(
            "PDF DO ORÇAMENTO:",
            type=["pdf"],
            accept_multiple_files=False
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
            "NUMERO_PEDIDO": numero_pedido,
            "NOME_CLIENTE": nome_cliente,
            "VENDEDOR": vendedor,
            "MEDIDAS_PORTA": medidas_porta,
            "LARGURA_BATENTE": largura_batente,
            "LADO_ABERTURA": lado_abertura,
            "ABRE_PARA": abre_para,
            "VENDO_DE": vendo_de
        }

        with st.spinner("Gerando pedido..."):

            resposta = enviar_pedido_porta(dados)

        st.write(resposta)

        #if resposta.get("success"):
            
            ##st.success("Pedido enviado com sucesso")

        #else:

            #st.error("Erro ao gerar pedido")
