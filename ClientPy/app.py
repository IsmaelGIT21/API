from flask import Flask, render_template, request, redirect, url_for, flash
from api_client import enviar_para_api
from api_client import enviar_para_api, buscar_vendas

app = Flask(__name__)
app.secret_key = 'chave_secreta_aqui'

@app.route('/', methods=['GET'])
def index():
    vendas = buscar_vendas()
    return render_template('index.html', vendas=vendas)
@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form.get('nome')
    quantidade = request.form.get('quantidade')
    valor = request.form.get('valor')

    sucesso = enviar_para_api(nome, quantidade, valor)

    if sucesso:
        flash('Produto cadastrado com sucesso!', 'sucesso')
    else:
        flash('Erro ao cadastrar produto na API.', 'erro')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)