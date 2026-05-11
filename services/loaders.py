import pandas as pd
import streamlit as st


# ===============================================
#  CARREGAR PRODUTO
# ===============================================
@st.cache_data
def carregar_clientes():

    df = pd.read_excel("Clientes_tratado.xlsx")

    # ==========================================
    # NORMALIZAR COLUNAS
    # ==========================================

    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
    )

    # ==========================================
    # COLUNA DE BUSCA OTIMIZADA
    # ==========================================

    colunas_busca = [
        "NOME",
        "NOME FANTASIA",
        "CNPJ",
    ]
    
    df["BUSCA"] = (
        df[colunas_busca]
        .fillna("")
        .astype(str)
        .apply(lambda linha: " ".join(linha), axis=1)
        .apply(limpar_texto)
    )

    return df



# ===============================================
#  CARREGAR CLIENTE
# ===============================================
@st.cache_data
def carregar_produtos():

    df = pd.read_excel("Produtos.xlsx")

    # ==========================================
    # NORMALIZAR COLUNAS
    # ==========================================

    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
    )

    # ==========================================
    # COLUNA DE BUSCA OTIMIZADA
    # ==========================================

    df["BUSCA"] = (
        df.fillna("")
        .astype(str)
        .apply(lambda linha: " ".join(linha), axis=1)
        .apply(limpar_texto)
    )

    return df
