import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/library/d/1oPNNDHDgHlb5FpqLUvNb5zwhVH-6zVpaqYLtfLMKpZq9EbPRz8aDB55x/3"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

