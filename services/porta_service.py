import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxIG18Cesqr4UAIuJX_nX1C5C4WnBq-1Q9nxBUFaQTe4tx-cyS7C1yyREyIXytWu3MavA/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

