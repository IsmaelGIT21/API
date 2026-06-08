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
        } else {
            console.error(data);
            alert('Erro ao cadastrar venda');
        }

    } catch (error) {
        console.error('Erro de conexão:', error);
        alert('Erro ao conectar com o servidor');
    }
}