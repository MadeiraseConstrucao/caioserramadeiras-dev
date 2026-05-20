import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxuleuN82zNZNevGAhwmdxdglg74DnKhZSv5LWgpGqUyOMnL2hhh__YGBP5NVOrUEEnmg/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

