import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzeadb3308jmUg1YBHSGB2XEA-fJ8JKNMKQ2QRe3hvqL5EDSPUDM6rU4LvWMJPQF2UwQQ/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

