<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\VendaController;

Route::get('/vendas', [VendaController::class, 'index']);
Route::post('/vendas', [VendaController::class, 'store']);