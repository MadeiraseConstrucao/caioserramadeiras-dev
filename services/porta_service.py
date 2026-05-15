import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbyXnXdbyDbiwdWeOAWD3R0TowUtKClFKm6aDlv_rW9KFQf4sYYW57P-ShhVKrzRFGp08w/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

