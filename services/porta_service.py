import requests


def enviar_pedido_porta(dados):

    WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwy1ieMLiQlEj5vR_jdW7pTu2SaGpHDrJOug5tYqMSpsRD2xlG6njXUCtJW_m_3k1lEfw/exec"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return {
        "status_code": response.status_code,
        "texto": response.text
    }

