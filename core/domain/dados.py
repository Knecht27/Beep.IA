
# Fabricantes de BIOS suportados
FABRICANTES_BIOS = {
    'ami': 'AMI (American Megatrends)',
    'award': 'Award BIOS',
    'phoenix': 'Phoenix BIOS',
    'ibm': 'IBM BIOS',
    'dell': 'Dell BIOS',
    'asus': 'ASUS BIOS',
    'gigabyte': 'GIGABYTE BIOS',
    'msi': 'MSI BIOS',
    'hp': 'HP/Compaq BIOS',
    'desconhecido': 'Desconhecido/Não sei'
}

# Fatos de beeps organizados por fabricante
BIPES_POR_FABRICANTE = {
    'ami': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória',
        'bipes_3_curtos': '3 beeps curtos - Erro nos primeiros 64KB de memória',
        'bipes_4_curtos': '4 beeps curtos - Timer do sistema falhou',
        'bipes_5_curtos': '5 beeps curtos - Erro no processador',
        'bipes_6_curtos': '6 beeps curtos - Erro no controlador de teclado',
        'bipes_7_curtos': '7 beeps curtos - Erro no modo virtual',
        'bipes_8_curtos': '8 beeps curtos - Erro na memória de vídeo',
        'bipes_1_longo': '1 beep longo - Erro de memória',
        'bipes_1_longo_1_curto': '1 beep longo, 1 curto - Problema na placa-mãe',
        'bipes_1_longo_2_curto': '1 beep longo, 2 curtos - Erro de vídeo (BIOS AMI)',
        'bipes_1_longo_3_curto': '1 beep longo, 3 curtos - Erro de memória RAM (BIOS AMI)',
        'bipes_1_longo_4_curto': '1 beep longo, 4 curtos - Sem placa de vídeo',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na fonte ou placa-mãe',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'award': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória (BIOS Award)',
        'bipes_1_longo': '1 beep longo - Erro de memória',
        'bipes_1_longo_2_curto': '1 beep longo, 2 curtos - Erro de vídeo',
        'bipes_1_longo_3_curto': '1 beep longo, 3 curtos - Erro de vídeo',
        'bipes_continuos': 'Beeps contínuos - Problema na memória ou placa de vídeo',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na fonte ou placa-mãe',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'phoenix': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_1_1_1': '1-1-1 (1 curto, pausa, 1 curto, pausa, 1 curto) - Erro na CPU',
        'bipes_1_1_2': '1-1-2 (1 curto, pausa, 1 curto, pausa, 2 curtos) - Erro na CPU',
        'bipes_1_1_3': '1-1-3 (1 curto, pausa, 1 curto, pausa, 3 curtos) - Erro na CMOS',
        'bipes_1_1_4': '1-1-4 (1 curto, pausa, 1 curto, pausa, 4 curtos) - Erro no BIOS',
        'bipes_1_2_1': '1-2-1 (1 curto, pausa, 2 curtos, pausa, 1 curto) - Erro no timer',
        'bipes_1_2_2': '1-2-2 (1 curto, pausa, 2 curtos, pausa, 2 curtos) - Erro na DMA',
        'bipes_1_2_3': '1-2-3 (1 curto, pausa, 2 curtos, pausa, 3 curtos) - Erro na DMA',
        'bipes_1_3_1': '1-3-1 (1 curto, pausa, 3 curtos, pausa, 1 curto) - Erro na memória',
        'bipes_1_3_3': '1-3-3 (1 curto, pausa, 3 curtos, pausa, 3 curtos) - Erro na memória',
        'bipes_continuos': 'Beeps contínuos - Problema na memória ou placa de vídeo',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'ibm': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação',
        'bipes_1_longo': '1 beep longo - Problema na placa-mãe',
        'bipes_1_longo_1_curto': '1 beep longo, 1 curto - Problema na placa-mãe',
        'bipes_1_longo_2_curto': '1 beep longo, 2 curtos - Erro de vídeo',
        'bipes_1_longo_3_curto': '1 beep longo, 3 curtos - Erro de vídeo',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória',
        'bipes_3_longos': '3 beeps longos - Erro de memória RAM',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'dell': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_2_curtos': '2 beeps curtos - RAM não detectada (BIOS Dell)',
        'bipes_3_curtos': '3 beeps curtos - Problema na placa-mãe (BIOS Dell)',
        'bipes_4_curtos': '4 beeps curtos - Erro na memória RAM (BIOS Dell)',
        'bipes_5_curtos': '5 beeps curtos - Problema no relógio em tempo real (BIOS Dell)',
        'bipes_6_curtos': '6 beeps curtos - Erro no chipset da placa-mãe (BIOS Dell)',
        'bipes_7_curtos': '7 beeps curtos - Erro no processador (BIOS Dell)',
        'bipes_8_curtos': '8 beeps curtos - Erro na placa de vídeo (BIOS Dell)',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação (BIOS Dell)',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'asus': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_1_longo': '1 beep longo - Problema na memória RAM (BIOS ASUS)',
        'bipes_1_longo_2_curtos': '1 beep longo, 2 curtos - Erro na placa de vídeo (BIOS ASUS)',
        'bipes_1_longo_3_curtos': '1 beep longo, 3 curtos - Erro na placa de vídeo (BIOS ASUS)',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória (BIOS ASUS)',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação (BIOS ASUS)',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na memória RAM (BIOS ASUS)',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'gigabyte': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_1_longo': '1 beep longo - Problema na memória RAM (BIOS GIGABYTE)',
        'bipes_1_longo_2_curtos': '1 beep longo, 2 curtos - Erro na placa de vídeo (BIOS GIGABYTE)',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória (BIOS GIGABYTE)',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação (BIOS GIGABYTE)',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na memória RAM (BIOS GIGABYTE)',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'msi': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_1_longo': '1 beep longo - Problema na memória RAM (BIOS MSI)',
        'bipes_1_longo_2_curtos': '1 beep longo, 2 curtos - Erro na placa de vídeo (BIOS MSI)',
        'bipes_1_longo_3_curtos': '1 beep longo, 3 curtos - Erro na placa de vídeo (BIOS MSI)',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória (BIOS MSI)',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação (BIOS MSI)',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na memória RAM (BIOS MSI)',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'hp': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_2_curtos': '2 beeps curtos - Erro de paridade na memória (BIOS HP/Compaq)',
        'bipes_3_curtos': '3 beeps curtos - Erro na memória base (BIOS HP/Compaq)',
        'bipes_4_curtos': '4 beeps curtos - Timer do sistema falhou (BIOS HP/Compaq)',
        'bipes_5_curtos': '5 beeps curtos - Erro no processador (BIOS HP/Compaq)',
        'bipes_1_longo': '1 beep longo - Erro de memória (BIOS HP/Compaq)',
        'bipes_1_longo_2_curtos': '1 beep longo, 2 curtos - Erro na placa de vídeo (BIOS HP/Compaq)',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte de alimentação (BIOS HP/Compaq)',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    },
    'desconhecido': {
        'bipes_1_curto': '1 beep curto - POST bem-sucedido',
        'bipes_continuos': 'Beeps contínuos - Problema na fonte ou placa-mãe',
        'bipes_continuos_curtos': 'Beeps curtos contínuos - Problema na fonte ou placa-mãe',
        'bipes_1_longo_2_curto': '1 beep longo, 2 curtos - Erro de vídeo',
        'bipes_1_longo_3_curto': '1 beep longo, 3 curtos - Erro de memória',
        'bipes_3_longos': '3 beeps longos - Erro de memória',
        'sem_bipes': 'Nenhum beep - Problema na fonte de alimentação ou placa-mãe'
    }
}

# Outros erros e problemas (não relacionados a beeps específicos)
OUTROS_ERROS = {
    'sem_video': 'Computador não exibe imagem na tela',
    'reiniciando': 'Computador reinicia sozinho',
    'superaquecimento': 'Temperatura elevada detectada',
    'nao_liga': 'Computador não liga',
    'cheiro_queimado': 'Odor de queimado presente',
    'tela_azul': 'Tela azul da morte (BSOD)',
    'lento': 'Sistema muito lento',
    'travando': 'Sistema trava/freeza',
    'ruido_estranho': 'Ruído estranho vindo do computador'
}


def obter_bipes_fabricante(fabricante):
    """Retorna os beeps disponíveis para um fabricante específico"""
    return BIPES_POR_FABRICANTE.get(fabricante, {})


def obter_todos_fatos():
    """Retorna todos os fatos disponíveis (beeps + outros erros)"""
    todos = {}
    for fabricante_bipes in BIPES_POR_FABRICANTE.values():
        todos.update(fabricante_bipes)
    todos.update(OUTROS_ERROS)
    return todos

