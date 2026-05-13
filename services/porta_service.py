import requests


# ==========================================
# ENVIAR PEDIDO
# ==========================================

def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/u/0/home/projects/1oPNNDHDgHlb5FpqLUvNb5zwhVH-6zVpaqYLtfLMKpZq9EbPRz8aDB55x/edit"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return response.json()
