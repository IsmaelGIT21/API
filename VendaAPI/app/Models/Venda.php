<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Venda extends Model
{
    protected $fillable = [
        'cliente_nome',
        'forma_pagamento',
        'produto_id', // Chave estrangeira ligada ao produto
        'quantidade',
        'valor',
    ];

    public function produto()
    {
        return $this->belongsTo(Produto::class, 'produto_id');
    }
}
