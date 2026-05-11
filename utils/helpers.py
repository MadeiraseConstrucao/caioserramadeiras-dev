import pandas as pd


def tratar(valor, padrao=""):

    if pd.isna(valor):
        return padrao

    valor = str(valor).strip()

    return valor if valor else padrao
