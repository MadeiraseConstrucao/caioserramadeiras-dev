import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycby4LCjAR56sbnwkR_VURjRt_DoEWMXhzyXmvH4mvpuH4G_4hc0DywJPdE5YXmtfRF3Mkw/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

