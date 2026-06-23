# 🛒 Sistema de Simulação de Vendas Distribuído

Este projeto consiste em um ecossistema distribuído de gerenciamento de vendas comerciais, desenvolvido como projeto final para a disciplina. O sistema demonstra a interoperabilidade e independência de plataforma através de uma **API RESTful** centralizada que se conecta a dois clientes (*clients*) independentes rodando em ecossistemas diferentes (Navegador Web e Python/Flask).

---

## 🚀 Arquitetura do Sistema

*   **Back-end (Servidor):** Desenvolvido em PHP com o framework **Laravel** (Porta `8000`), responsável pelas regras de negócio e persistência de dados.
*   **Banco de Dados:** Banco relacional **MySQL** gerenciado via Eloquent ORM.
*   **Client 1 (Web / JS):** Interface gráfica construída em HTML/CSS e JavaScript Vanilla utilizando `Fetch API` para comunicação assíncrona.
*   **Client 2 (Python / Flask):** Interface secundária construída em Python com o microframework **Flask** (Porta `5000`) e biblioteca `requests` para chamadas servidor-para-servidor.

---

## 🛠️ Como Executar o Projeto

Siga a ordem dos passos abaixo para colocar todo o ecossistema para rodar localmente no seu computador.

### 1. Configurando e Iniciando o Servidor (Laravel)
Abra o seu terminal na pasta raiz do projeto Laravel e execute os comandos:

```bash
# Instalar as dependências do PHP (caso necessário)
composer install

# Configurar o banco de dados e recriar as tabelas do zero
php artisan migrate:fresh

# Iniciar o servidor local do Laravel
php artisan serve
```
O servidor estará ativo em: `http://127.0.0.1:8000`

### 2. Executando o Client 1 (Web / JavaScript)
1. Certifique-se de que a extensão **Live Server** está instalada no seu VS Code.
2. Abra o arquivo `index.html` do seu cliente Web.
3. Clique com o botão direito no código e escolha **"Open with Live Server"**.
A aplicação abrirá no seu navegador, geralmente na porta `5501`.

### 3. Executando o Client 2 (Python / Flask)
Abra um **novo terminal** na pasta do projeto Python (`ClientPy`) e execute os comandos:

```bash
# Entrar no diretório do projeto Python
cd ClientPy

# Ativar o ambiente virtual (Virtual Environment)
source venv/bin/activate

# Iniciar a aplicação Flask
python app.py
```
O cliente Python estará ativo em: `http://127.0.0.1:5000`

---

## 🗄️ Estrutura do JSON Praticado (Payload)

Para realizar o cadastro de uma nova venda em qualquer um dos clientes, o servidor espera receber um objeto estruturado no seguinte formato JSON via método **POST** no endpoint `/api/vendas`:

```json
{
    "cliente_nome": "Ismael Elger",
    "forma_pagamento": "Pix",
    "produto_id": 1,
    "quantidade": 2,
    "valor": 250.00
}
```

---
*   Ismael Felipe