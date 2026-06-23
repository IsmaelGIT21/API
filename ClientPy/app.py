from flask import Flask, render_template, request, redirect, url_for, flash
from api_client import enviar_para_api, buscar_vendas, buscar_produtos

app = Flask(__name__)
app.secret_key = 'chave_secreta_aqui'

@app.route('/', methods=['GET'])
def index():
    vendas = buscar_vendas()
    produtos = buscar_produtos() 
    return render_template('index.html', vendas=vendas, produtos=produtos)

@app.route('/enviar', methods=['POST'])
def enviar():
    cliente_nome = request.form.get('cliente_nome')
    forma_pagamento = request.form.get('forma_pagamento')
    produto_id = request.form.get('produto_id')
    quantidade = request.form.get('quantidade')
    valor = request.form.get('valor')

    sucesso = enviar_para_api(cliente_nome, forma_pagamento, produto_id, quantidade, valor)

    if sucesso:
        flash('Venda cadastrada com sucesso!', 'sucesso')
    else:
        flash('Erro ao cadastrar venda na API.', 'erro')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
