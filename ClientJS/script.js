const IP_ATUAL = window.location.hostname; 
const PORTA_LARAVEL = window.location.port === "8000" ? "8080" : "8000";
const API_URL = `http://${IP_ATUAL}:${PORTA_LARAVEL}/api`;
window.onload = () => {
    carregarProdutos(); 
    carregarVendas();
};

async function carregarProdutos() {
    try {
        const response = await fetch(`${API_URL}/produtos`);
        if (!response.ok) return;
        const produtos = await response.json();
        
        const select = document.getElementById('produto_id');
        select.innerHTML = '<option value="">Selecione...</option>';
        
        produtos.forEach(p => {
            select.innerHTML += `<option value="${p.id}">${p.nome}</option>`;
        });
    } catch (error) {
        console.error('Erro ao buscar produtos:', error);
    }
}

async function cadastrarVenda() {
    const venda = {
        cliente_nome: document.getElementById('cliente_nome').value,
        forma_pagamento: document.getElementById('forma_pagamento').value,
        produto_id: parseInt(document.getElementById('produto_id').value) || 1,
        quantidade: parseInt(document.getElementById('quantidade').value) || 1,
        valor: parseFloat(document.getElementById('valor').value) || 0
    };

    try {
        const response = await fetch(`${API_URL}/vendas`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify(venda)
        });

        if (response.ok) {
            alert('Venda cadastrada com sucesso!');
            carregarVendas();
        } else {
            alert('Erro no servidor Laravel ao cadastrar');
        }
    } catch (error) {
        alert('Erro de conexão: Garanta que o php artisan serve está rodando.');
    }
}

async function carregarVendas() {
    try {
        const response = await fetch(`${API_URL}/vendas`);
        if (!response.ok) return;
        const vendas = await response.json();

        const lista = document.getElementById('listaVendas');
        lista.innerHTML = '';

        vendas.forEach(v => {
            lista.innerHTML += `<li>${v.cliente_nome} - Qtd: ${v.quantidade} - Valor: R$ ${parseFloat(v.valor).toFixed(2)}</li>`;
        });
    } catch (error) {
        console.error('Erro ao conectar na API:', error);
    }
}
