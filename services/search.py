from utils.helpers import limpar_texto

# =====================================================
#  DATAFRAME
# =====================================================
def buscar_dataframe(df, busca):

    busca_limpa = limpar_texto(busca)

    resultado = df[
        df["BUSCA"].str.contains(busca_limpa, na=False)
    ].copy()

    # ==========================================
    # PRIORIDADE
    # ==========================================

    resultado["PRIORIDADE"] = resultado["BUSCA"].apply(
        lambda x: 0 if x.startswith(busca_limpa) else 1
    )

    resultado = resultado.sort_values(
        by="PRIORIDADE"
    )

    return resultado
