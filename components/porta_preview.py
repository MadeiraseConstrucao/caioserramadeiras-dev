import os


# ==========================================
# IMAGEM ORIENTAÇÃO PORTA
# ==========================================

def obter_imagem_porta(
    lado_abertura,
    abre_para,
    vendo_de
):

    chave = (
        f"{lado_abertura}|{abre_para}|{vendo_de}"
        .upper()
        .strip()
    )

    imagens = {
        "DIREITA|FORA DO AMBIENTE|DENTRO": "PORTA_DIREITA_FORA.png",
        "ESQUERDA|FORA DO AMBIENTE|DENTRO": "PORTA_ESQUERDA_FORA.png",
        "DIREITA|DENTRO DO AMBIENTE|DENTRO": "PORTA_ESQUERDA_DENTRO.png",
        "ESQUERDA|DENTRO DO AMBIENTE|DENTRO": "PORTA_DIREITA_DENTRO.png",
        "DIREITA|FORA DO AMBIENTE|FORA": "PORTA_ESQUERDA_FORA.png",
        "ESQUERDA|FORA DO AMBIENTE|FORA": "PORTA_DIREITA_FORA.png",
        "DIREITA|DENTRO DO AMBIENTE|FORA": "PORTA_DIREITA_DENTRO.png",
        "ESQUERDA|DENTRO DO AMBIENTE|FORA": "PORTA_ESQUERDA_DENTRO.png"
    }

    nome_imagem = imagens.get(chave)

    if not nome_imagem:
        return None

    return os.path.join(
        "assets",
        "portas",
        nome_imagem
    )
