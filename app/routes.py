from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from .email import enviar_email

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form.get('usuario')

        if not usuario:
            flash('Digite o usuário cadastrado!', 'warning')
            return redirect(url_for('main.index'))

        prontuario = current_app.config['PRONTUARIO_FIXO']
        nome = current_app.config['NOME_FIXO']

        # Envia o e-mail via Mailgun
        enviar_email(prontuario, nome, usuario)
        flash('Cadastro enviado com sucesso!', 'success')

        return redirect(url_for('main.index'))

    return render_template('index.html')
