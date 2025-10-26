import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # Configurações do Mailgun
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
    MAILGUN_FROM = os.environ.get('MAILGUN_FROM')

    # E-mails de destino
    ADMIN_EMAIL = 'flaskaulasweb@zohomail.com'
    EMAIL_INSTITUCIONAL = os.environ.get('EMAIL_INSTITUCIONAL') 


    PRONTUARIO_FIXO = 'PT3032621'
    NOME_FIXO = 'Gustavo Máximo Da Silva'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
