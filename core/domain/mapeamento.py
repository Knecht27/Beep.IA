# Mapeamento de conclusões para fatos derivados (para forward chaining)
MAPEAMENTO_CONCLUSAO_FATO = {
    'problema_memoria_ram': [
        'Erro de memória RAM',
        'problema na memória RAM',
        'memória RAM defeituosa',
        'módulos de memória defeituosos'
    ],
    'problema_placa_video': [
        'Erro de vídeo',
        'placa de vídeo defeituosa',
        'problema na placa de vídeo',
        'Erro na placa de vídeo'
    ],
    'problema_processador': [
        'Erro no processador',
        'CPU defeituosa',
        'problema no processador',
        'Erro na CPU'
    ],
    'problema_placa_mae': [
        'Problema na placa-mãe',
        'placa-mãe defeituosa',
        'problema na placa mãe'
    ],
    'problema_fonte': [
        'fonte de alimentação defeituosa',
        'problema na fonte',
        'fonte de alimentação'
    ]
}


def extrair_fatos_da_conclusao(conclusao):
    """Extrai fatos derivados de uma conclusão para forward chaining"""
    fatos_extraidos = []
    conclusao_lower = conclusao.lower()
    
    for fato, palavras_chave in MAPEAMENTO_CONCLUSAO_FATO.items():
        for palavra_chave in palavras_chave:
            if palavra_chave.lower() in conclusao_lower:
                if fato not in fatos_extraidos:
                    fatos_extraidos.append(fato)
                break
    
    return fatos_extraidos

