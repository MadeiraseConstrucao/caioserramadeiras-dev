import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwizt6tcLjhi5eaiApUGdInJIYN2OSn6__hjHgUi_kmqqHP3roDEGNvIAYhcyLGXIelng/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

