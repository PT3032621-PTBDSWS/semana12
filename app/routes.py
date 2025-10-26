from flask import Blueprint, render_template, request, flash, redirect, url_for
from .email import enviar_email

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prontuario = request.form.get('prontuario')
        nome = request.form.get('nome')
        usuario = request.form.get('usuario')

        if not all([prontuario, nome, usuario]):
            flash('Preencha todos os campos!', 'warning')
            return redirect(url_for('main.index'))

        # Envia o e-mail
        enviar_email(prontuario, nome, usuario)
        flash('Cadastro enviado com sucesso!', 'success')

    return render_template('index.html')
