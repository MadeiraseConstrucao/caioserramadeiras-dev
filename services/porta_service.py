import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxUKRGt4CegyzEPSk-yd4LVjavTcyQHssO_lMZTFbwMfRQGRd48VeetexNbEMZm1QjDJw/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

