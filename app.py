# Código Refatorado — Consulta Pangeia


# ==========================================
# IMPORTS
# ==========================================

import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import re
import base64
import unicodedata

# ==========================================
# CONFIG
# ==========================================

st.set_page_config(
    page_title="Consulta Pangeia",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CSS GLOBAL
# ==========================================

def carregar_css():

    with open("assets/styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

carregar_css()

# ==========================================
# FUNÇÕES
# ==========================================

def tratar(valor, padrao=""):

    if pd.isna(valor):
        return padrao

    valor = str(valor).strip()

    return valor if valor else padrao


def limpar_texto(texto):

    texto = str(texto).lower()

    texto = unicodedata.normalize("NFKD", texto)
    texto = texto.encode("ASCII", "ignore").decode("utf-8")

    return re.sub(r'[^0-9a-zA-Z]', '', texto)


def mostrar_logo(caminho, largura=180):

    with open(caminho, "rb") as img:
        b64 = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <div style="text-align:center; margin-bottom:25px;">
        <img src="data:image/png;base64,{b64}" width="{largura}">
    </div>
    """, unsafe_allow_html=True)


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


def mostrar_sem_busca():

    st.markdown("""
    <div class="sem-busca">
        🔎 Digite algo para pesquisar
    </div>
    """, unsafe_allow_html=True)


def mostrar_total_resultados(total):

    st.markdown(f"""
    <div class="resultado">
    <b>Resultados encontrados:</b> {total}
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# CARREGAR DADOS
# ==========================================

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

# ==========================================
# DATAFRAMES
# ==========================================

with st.spinner("Carregando sistema..."):

    df_clientes = carregar_clientes()
    df_produtos = carregar_produtos()

# ==========================================
# SESSION STATE
# ==========================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "menu"

if "busca_cliente" not in st.session_state:
    st.session_state.busca_cliente = ""

if "busca_produto" not in st.session_state:
    st.session_state.busca_produto = ""

# ==========================================
# SIDEBAR
# ==========================================

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

# ==========================================
# MENU PRINCIPAL
# ==========================================

def pagina_menu():

    st.markdown(
        "<div class='main-title'>CONSULTA PANGEIA</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Sistema de consulta interna</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # ==========================================
    # CLIENTES
    # ==========================================

    with col1:

        st.markdown("### 👥 Clientes")

        st.markdown(
            "Consulta rápida por Nome, CNPJ e CPF."
        )

        if st.button(
            "ABRIR CONSULTA CLIENTES",
            use_container_width=True
        ):

            st.session_state.pagina = "clientes"
            st.rerun()

    # ==========================================
    # PRODUTOS
    # ==========================================

    with col2:

        st.markdown("### 📦 Produtos")

        st.markdown(
            "Consulta de produtos por Descrição, NCM, Unidade e Preço."
        )

        if st.button(
            "ABRIR CONSULTA PRODUTOS",
            use_container_width=True
        ):

            st.session_state.pagina = "produtos"
            st.rerun()

# ==========================================
# CARD CLIENTE
# ==========================================

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
    """

    components.html(card_html, height=550)




# ==========================================
# PÁGINA CLIENTES
# ==========================================

def pagina_clientes():

    st.markdown(
        "<div class='section-title'>👥 CONSULTA DE CLIENTES</div>",
        unsafe_allow_html=True
    )

    busca = st.text_input(
        "🔎 Buscar cliente",
        key="busca_cliente",
        placeholder="Digite nome, CNPJ..."
    )

    if not busca:

        mostrar_sem_busca()
        return

    with st.spinner("Pesquisando clientes..."):

        resultado = buscar_dataframe(df_clientes, busca)

        resultado = resultado.head(50)

    mostrar_total_resultados(len(resultado))

    for _, row in resultado.iterrows():

        renderizar_card_cliente(row)

# ==========================================
# CARD PRODUTO
# ==========================================

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

# ==========================================
# PÁGINA PRODUTOS
# ==========================================

def pagina_produtos():

    st.markdown(
        "<div class='section-title'>📦 CONSULTA DE PRODUTOS</div>",
        unsafe_allow_html=True
    )

    busca = st.text_input(
        "🔎 Buscar produto",
        key="busca_produto",
        placeholder="Digite descrição, NCM, unidade..."
    )
    

    if not busca:

        mostrar_sem_busca()
        return

    with st.spinner("Pesquisando produtos..."):

        resultado = buscar_dataframe(
            df_produtos,
            busca
        )

        resultado = resultado.head(50)

    mostrar_total_resultados(len(resultado))

    # ==========================================
    # GRID RESPONSIVO
    # ==========================================

    colunas = st.columns(2)

    for i, (_, row) in enumerate(resultado.iterrows()):

        with colunas[i % 2]:

            renderizar_card_produto(row)

# ==========================================
# ROTEAMENTO
# ==========================================

if st.session_state.pagina == "menu":

    pagina_menu()

elif st.session_state.pagina == "clientes":

    pagina_clientes()

elif st.session_state.pagina == "produtos":

    pagina_produtos()

