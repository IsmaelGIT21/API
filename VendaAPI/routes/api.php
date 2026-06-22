<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\VendaController;
use App\Models\Produto; // Importa a Model de Produto

// Rota antiga de vendas (Mantida)
Route::get('/vendas', [VendaController::class, 'index']);
Route::post('/vendas', [VendaController::class, 'store']);

// 🚀 A ROTA QUE FALTAVA: Entrega a lista de produtos para o select do JavaScript
Route::get('/produtos', function () {
    return response()->json(Produto::all());
});
