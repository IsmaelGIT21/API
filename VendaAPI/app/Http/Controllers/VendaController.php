<?php

namespace App\Http\Controllers;

use App\Models\Venda;
use Illuminate\Http\Request;

class VendaController extends Controller
{
    public function index()
    {
        $vendas = Venda::all();
        return response()->json($vendas);
    }

    public function store(Request $request)
    {
        $venda = Venda::create([
            'cliente_nome'    => $request->cliente_nome,
            'forma_pagamento' => $request->forma_pagamento,
            'produto_id'      => $request->produto_id, 
            'quantidade'      => $request->quantidade,
            'valor'           => $request->valor, 
        ]);

        return response()->json([
            'message' => 'Venda criada com sucesso',
            'venda' => $venda
        ], 201);
    }
}
