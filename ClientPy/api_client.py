import requests

API_URL = "http://127.0.0.1:8000/api/vendas"

def enviar_para_api(nome, quantidade, valor):
    dados = {
        "produto": nome,
        "quantidade": int(quantidade),
        "valor": float(valor)
    }
    try:
        resposta = requests.post(API_URL, json=dados, timeout=5)
        
        print("\n--- DIAGNÓSTICO DE ENVIO ---", flush=True)
        print(f"Dados enviados: {dados}", flush=True)
        print(f"Status retornado pela API: {resposta.status_code}", flush=True)
        print(f"Resposta bruta da API: {resposta.text}", flush=True)
        print("----------------------------\n", flush=True)
        
        return resposta.status_code in range(200, 300)
    except requests.exceptions.RequestException as e:
        print("\n--- ERRO DE CONEXÃO ---", flush=True)
        print(f"Não foi possível falar com a API: {e}", flush=True)
        print("-----------------------\n", flush=True)
        return False
        
def buscar_vendas():
    try:
        resposta = requests.get(API_URL, timeout=5)

        print("\n--- GET VENDAS ---", flush=True)
        print(f"Status: {resposta.status_code}", flush=True)
        print(f"Resposta: {resposta.text}", flush=True)
        print("------------------\n", flush=True)

        if resposta.status_code == 200:
            return resposta.json()
        return []

    except requests.exceptions.RequestException as e:
        print("\n--- ERRO GET ---", flush=True)
        print(e, flush=True)
        print("----------------\n", flush=True)
        return []