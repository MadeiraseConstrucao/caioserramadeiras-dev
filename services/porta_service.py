import requests


# ==========================================
# ENVIAR PEDIDO
# ==========================================

def enviar_pedido_porta(dados):

    WEBHOOK_URL = "COLOCAR_URL_APPS_SCRIPT"

    response = requests.post(
        WEBHOOK_URL,
        json=dados,
        timeout=60
    )

    return response.json()
