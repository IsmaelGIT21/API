async function cadastrarVenda() {
    const produto = document.getElementById('produto').value;
    const quantidade = document.getElementById('quantidade').value;
    const valor = document.getElementById('valor').value;

    const venda = {
        produto,
        quantidade: parseInt(quantidade),
        valor: parseFloat(valor)
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/vendas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(venda)
        });

        const data = await response.json();

        if (response.ok) {
            alert('Venda cadastrada com sucesso!');
            limparCampos();
            carregarVendas(); // atualiza lista
        } else {
            console.error(data);
            alert('Erro ao cadastrar venda');
        }

    } catch (error) {
        console.error('Erro de conexão:', error);
        alert('Erro ao conectar com o servidor');
    }
}


// 🔥 LISTAR VENDAS (GET)
async function carregarVendas() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/vendas');
        const vendas = await response.json();

        const lista = document.getElementById('listaVendas');
        lista.innerHTML = '';

        vendas.forEach(venda => {
            const item = document.createElement('li');

            item.innerHTML = `
                <strong>${venda.produto}</strong> -
                Qtd: ${venda.quantidade} -
                Valor: R$ ${parseFloat(venda.valor).toFixed(2)}
            `;

            lista.appendChild(item);
        });

    } catch (error) {
        console.error('Erro ao buscar vendas:', error);
    }
}


// limpar campos
function limparCampos() {
    document.getElementById('produto').value = '';
    document.getElementById('quantidade').value = '';
    document.getElementById('valor').value = '';
}