import requests
from flask import current_app

def enviar_email(prontuario, nome, usuario):
    """
    Envia e-mail via API do Mailgun para o endereço do professor
    e o e-mail institucional configurado no config.py
    """
    api_key = current_app.config['MAILGUN_API_KEY']
    domain = current_app.config['MAILGUN_DOMAIN']
    sender = current_app.config['MAILGUN_FROM']
    admin_email = current_app.config['ADMIN_EMAIL']
    institucional = current_app.config['EMAIL_INSTITUCIONAL']

    subject = f'Novo usuário cadastrado: {usuario}'
    body = f"""
    Novo cadastro realizado!

    📘 Prontuário: {prontuario}
    👤 Nome: {nome}
    🧾 Usuário: {usuario}
    """

    # Envia para os dois destinatários
    for destinatario in [admin_email, institucional]:
        requests.post(
            f'https://api.mailgun.net/v3/{domain}/messages',
            auth=('api', api_key),
            data={
                'from': sender,
                'to': destinatario,
                'subject': subject,
                'text': body
            }
        )
