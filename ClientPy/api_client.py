import requests

URL_API = "http://127.0.0.1:8000/api"

def enviar_para_api(cliente_nome, forma_pagamento, produto_id, quantidade, valor):
    venda_payload = {
        "cliente_nome": cliente_nome,
        "forma_pagamento": forma_pagamento,
        "produto_id": int(produto_id) if produto_id else 1,
        "quantidade": int(quantidade) if quantidade else 1,
        "valor": float(valor) if valor else 0.0
    }

    try:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        resposta = requests.post(
            f"{URL_API}/vendas",
            json=venda_payload,
            headers=headers
        )

        print("POST STATUS:", resposta.status_code)
        print("POST RESPOSTA:", resposta.text)

        return resposta.status_code == 201

    except Exception as e:
        print(f"Erro no POST: {e}")
        return False

def buscar_vendas():
    try:
        headers = {'Accept': 'application/json'}

        resposta = requests.get(
            f"{URL_API}/vendas",
            headers=headers
        )

        print("STATUS VENDAS:", resposta.status_code)

        if resposta.status_code == 200:
            return resposta.json()

        return []

    except Exception as e:
        print(f"Erro no GET Vendas: {e}")
        return []

def buscar_produtos():
    try:
        headers = {'Accept': 'application/json'}

        resposta = requests.get(
            f"{URL_API}/produtos",
            headers=headers
        )

        print("STATUS PRODUTOS:", resposta.status_code)
        print("RESPOSTA PRODUTOS:", resposta.text)

        if resposta.status_code == 200:
            return resposta.json()

        return []

    except Exception as e:
        print(f"Erro no GET Produtos: {e}")
        return []