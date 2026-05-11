import pandas as pd
import streamlit as st
import re
import unicodedata
import base64



# ========================================
#  TRATAR
# ========================================
def tratar(valor, padrao=""):

    if pd.isna(valor):
        return padrao

    valor = str(valor).strip()

    return valor if valor else padrao
    

# ========================================
#  LIMPAR TEXTO
# ========================================
def limpar_texto(texto):

    texto = str(texto).lower()

    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ASCII", "ignore").decode("utf-8")

    return re.sub(r'[^0-9a-zA-Z]', '', texto)


# ========================================
#  FORMATAR PREÇO
# ========================================
def formatar_preco(valor_preco):

    if pd.isna(valor_preco):
        return "SEM PREÇO"

    try:

        if isinstance(valor_preco, (int, float)):

            preco_float = float(valor_preco)

        else:

            preco_texto = (
                str(valor_preco)
                .replace("R$", "")
                .replace(" ", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()
            )

            preco_float = float(preco_texto)

        return (
            f"R$ {preco_float:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

    except:

        return str(valor_preco)


# ========================================
#  MOSTRAR SEM BUSCA
# ========================================
def mostrar_sem_busca():

    st.markdown("""
    <div class="sem-busca">
        🔎 Digite algo para pesquisar
    </div>
    """, unsafe_allow_html=True)


# ========================================
#  MOSTRAR TOTAL DE R4ESULTADOS
# ========================================
def mostrar_total_resultados(total):

    st.markdown(f"""
    <div class="resultado">
    <b>Resultados encontrados:</b> {total}
    </div>
    """, unsafe_allow_html=True)


# ========================================
#  MOSTRAR LOGO
# ========================================
def mostrar_logo(caminho, largura=180):

    with open(caminho, "rb") as img:
        b64 = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <img src="data:image/png;base64,{b64}" width="{largura}">
    </div>
    """, unsafe_allow_html=True)

