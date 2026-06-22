<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
public function up(): void
{
    Schema::create('vendas', function (Blueprint $table) {
        $table->id();
        $table->string('cliente_nome');
        $table->string('forma_pagamento');
        
        // Vincula a venda obrigatoriamente a um ID existente na tabela de produtos
        $table->foreignId('produto_id')->constrained('produtos')->onDelete('cascade');
        
        $table->integer('quantidade');
        $table->decimal('valor', 10, 2); 
        $table->timestamps();
    });
}



    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('vendas');
    }
};
