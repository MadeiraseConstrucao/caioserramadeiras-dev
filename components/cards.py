import streamlit as st
import streamlit.components.v1 as components

from utils.helpers import (
    tratar,
    formatar_preco
)



# =================================================================
#  RENDERIZAR CARD CLIENTE
# =================================================================
def renderizar_card_cliente(row):

    nome_fantasia = row.get("NOME FANTASIA", "SEM NOME FANTASIA")
    razao_social = row.get("NOME", "")
    cnpj = row.get("CNPJ", "")
    ie = row.get("INSCRIÇÃO ESTADUAL", "")

    telefone = tratar(
        row.get("TELEFONE", ""),
        "SEM TELEFONE"
    )

    email = tratar(
        row.get("EMAIL", ""),
        "SEM EMAIL"
    )

    cidade = row.get("CIDADE", "")
    endereco = row.get("ENDEREÇO", "")
    bairro = row.get("BAIRRO", "")
    uf = row.get("UF", "")

    card_html = f"""        
    <div class="card">

        <h2>🏢 {razao_social}</h2>

        <hr>

        <p>
            <b>📄 Nome Fantasia:</b><br>
            {nome_fantasia}
        </p>

        <p>
            <b>🧾 CNPJ/CPF:</b><br>
            {cnpj}
        </p>

        <p>
            <b>📌 Inscrição Estadual:</b><br>
            {ie}
        </p>

        <p>
            <b>📞 Telefone:</b><br>
            {telefone}
        </p>

        <p>
            <b>📧 Email:</b><br>
            {email}
        </p>

        <p>
            <b>📍 Localização:</b><br>
            {endereco}, {bairro} - {cidade} / {uf}
        </p>

    </div>
    

    components.html(card_html, height=550)



# =================================================================
#  RENDERIZAR CARD PRODUTO
# =================================================================
def renderizar_card_produto(row):

    descricao = tratar(
        row.get("DESCRICAO", ""),
        "SEM DESCRIÇÃO"
    )

    und = tratar(
        row.get("UND", ""),
        "-"
    )

    # ==========================================
    # NCM
    # ==========================================

    try:

        ncm = int(row.get("NCM", 0))

    except:

        ncm = "-"

    # ==========================================
    # PREÇO
    # ==========================================

    preco = formatar_preco(
        row.get("PREÇO")
    )

    card_html = f"""
    <div class="card">

        <h2>📦 {descricao}</h2>

        <hr>

        <p>
            <b>📏 Unidade:</b><br>
            {und}
        </p>

        <p>
            <b>💰 Preço:</b><br>
            {preco}
        </p>

        <p>
            <b>🏷 NCM:</b><br>
            {ncm}
        </p>

    </div>
    """

    components.html(card_html, height=320)
