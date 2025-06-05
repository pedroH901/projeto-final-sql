import os
import uuid
import pyodbc
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp_cadastro_pet = Blueprint('cadastro_pet', __name__, template_folder='templates')

UPLOAD_FOLDER = 'static/uploads'

def conectar_bd():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=SEU_SERVIDOR;'
                          'DATABASE=SEU_BANCO;'
                          'UID=SEU_USUARIO;'
                          'PWD=SUA_SENHA')

@bp_cadastro_pet.route('/cadastro_pet', methods=['GET', 'POST'])
def cadastro_pet():
    if request.method == 'POST':
        especie = request.form['especie']
        situacao = request.form['situacao']
        data = request.form['data']
        sexo = request.form['sexo']
        cidade = request.form['cidade']
        bairro = request.form['bairro']
        descricao = request.form['descricao']
        id_usuario = 1  # Ajustar se tiver sistema de usuários

        foto = request.files['foto']
        caminho_foto = None

        if foto and foto.filename != '':
            nome_arquivo = f"{uuid.uuid4().hex}_{foto.filename}"
            caminho_foto = os.path.join(UPLOAD_FOLDER, nome_arquivo)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            foto.save(caminho_foto)

        try:
            conn = conectar_bd()
            cursor = conn.cursor()

            cursor.execute('''
                INSERT INTO pet (especie, situacao, foto, data, sexo, cidade, bairro, descricao, id_usuario)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (especie, situacao, caminho_foto, data, sexo, cidade, bairro, descricao, id_usuario))

            conn.commit()
            conn.close()

            flash('Pet cadastrado com sucesso!', 'success')
            return redirect(url_for('cadastro_pet.cadastro_pet'))

        except Exception as e:
            flash(f'Erro ao cadastrar pet: {str(e)}', 'danger')

    return render_template('cadastro_pet.html')
