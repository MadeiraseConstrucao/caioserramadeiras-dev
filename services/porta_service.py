import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbxxHa5lbBg5xCZBZa4Cx9t-GMHE_kaSRh22VWGcAIxCL2BEmWvk561yUFEo0PvRm2s3wg/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

