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
    return BIPES_POR_FABRICANTE.get(fabricante, {})

def obter_todos_fatos():
    todos = {}
    for fabricante_bipes in BIPES_POR_FABRICANTE.values():
        todos.update(fabricante_bipes)
    todos.update(OUTROS_ERROS)
    return todos

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
    fatos_extraidos = []
    conclusao_lower = conclusao.lower()
    
    for fato, palavras_chave in MAPEAMENTO_CONCLUSAO_FATO.items():
        for palavra_chave in palavras_chave:
            if palavra_chave.lower() in conclusao_lower:
                if fato not in fatos_extraidos:
                    fatos_extraidos.append(fato)
                break
    
    return fatos_extraidos

REGRAS = [
    # Regras relacionadas a beeps da BIOS - AMI
    ({'bipes_1_curto'}, 'POST bem-sucedido - Sistema funcionando normalmente. O computador passou por todos os testes de inicialização sem erros. Nenhuma ação necessária.'),
    
    ({'bipes_1_longo_2_curto'}, 'Erro de vídeo detectado (BIOS AMI). Possíveis causas: placa de vídeo defeituosa, conexão solta, monitor sem sinal, ou problema no slot PCIe/AGP. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Testar com outra placa de vídeo; 3) Verificar conexão do cabo de vídeo; 4) Testar o monitor em outro computador; 5) Limpar contatos da placa de vídeo com borracha.'),
    
    ({'bipes_1_longo_3_curto'}, 'Erro de memória RAM detectado (BIOS AMI). Possíveis causas: módulos de memória defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos com borracha; 4) Verificar compatibilidade da memória com a placa-mãe; 5) Testar com módulos conhecidamente funcionais; 6) Verificar se os módulos estão no slot correto (consultar manual da placa-mãe).'),
    
    ({'bipes_2_curtos'}, 'Erro de paridade na memória RAM. Indica falha na verificação de integridade dos dados na memória. Possíveis causas: módulo de memória defeituoso, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover módulos de memória e testar um por vez; 2) Verificar se a memória é compatível com a placa-mãe; 3) Limpar contatos dos módulos; 4) Testar com memória conhecidamente funcional; 5) Verificar se há atualização de BIOS disponível.'),
    
    ({'bipes_3_curtos'}, 'Erro nos primeiros 64KB de memória (BIOS AMI). Falha crítica na memória base do sistema. Possíveis causas: módulo de memória defeituoso, problema na placa-mãe, ou configuração incorreta. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Verificar se os módulos estão no slot correto (geralmente slot 1); 3) Limpar contatos dos módulos; 4) Testar com memória conhecidamente funcional; 5) Verificar configurações de memória no BIOS; 6) Considerar atualização do BIOS.'),
    
    ({'bipes_4_curtos'}, 'Timer do sistema falhou (BIOS AMI). Problema no circuito de temporização da placa-mãe. Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. Soluções: 1) Desligar o computador e desconectar da energia por alguns minutos; 2) Verificar se não há curto-circuito na placa-mãe; 3) Limpar a placa-mãe de poeira; 4) Verificar se todos os componentes estão bem conectados; 5) Considerar substituição da placa-mãe se o problema persistir.'),
    
    ({'bipes_5_curtos'}, 'Erro no processador detectado (BIOS AMI). Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. Soluções: 1) Verificar se o processador está bem encaixado no socket; 2) Verificar temperatura do processador; 3) Verificar se o cooler está funcionando corretamente; 4) Aplicar pasta térmica nova se necessário; 5) Verificar compatibilidade do processador com a placa-mãe; 6) Testar com outro processador compatível se possível.'),
    
    ({'bipes_6_curtos'}, 'Erro no controlador de teclado (BIOS AMI). Problema na comunicação com o teclado durante o POST. Possíveis causas: teclado defeituoso, conexão solta, ou problema na placa-mãe. Soluções: 1) Desconectar e reconectar o teclado; 2) Testar com outro teclado; 3) Verificar se o teclado está conectado na porta correta (PS/2 ou USB); 4) Limpar a porta de conexão; 5) Verificar se há curto-circuito no teclado; 6) Se usar adaptador USB-PS/2, testar sem ele.'),
    
    ({'bipes_7_curtos'}, 'Erro no modo virtual (BIOS AMI). Falha no processador ao entrar em modo de processamento virtual. Possíveis causas: CPU defeituosa, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Verificar se o processador está bem encaixado; 2) Verificar compatibilidade do processador; 3) Atualizar o BIOS para a versão mais recente; 4) Verificar configurações de virtualização no BIOS; 5) Testar com outro processador compatível se possível.'),
    
    ({'bipes_8_curtos'}, 'Erro na memória de vídeo (BIOS AMI). Problema na memória dedicada da placa de vídeo. Possíveis causas: placa de vídeo defeituosa, memória VRAM corrompida, ou superaquecimento. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar temperatura da placa de vídeo; 3) Limpar poeira do cooler da placa de vídeo; 4) Testar com outra placa de vídeo; 5) Verificar se há atualização de drivers disponível; 6) Considerar substituição da placa de vídeo se o problema persistir.'),
    
    ({'bipes_1_longo'}, 'Erro de memória RAM detectado. Falha geral na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir todos os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos com borracha; 4) Verificar compatibilidade da memória com a placa-mãe; 5) Testar com módulos conhecidamente funcionais; 6) Verificar se os módulos estão nos slots corretos conforme o manual da placa-mãe.'),
    
    ({'bipes_1_longo_1_curto'}, 'Problema na placa-mãe detectado (BIOS AMI). Falha geral no sistema base. Possíveis causas: placa-mãe defeituosa, curto-circuito, ou componente mal conectado. Soluções: 1) Desligar e desconectar da energia; 2) Verificar se não há curto-circuito (parafusos soltos, componentes em contato); 3) Remover e reinserir todos os componentes principais; 4) Limpar a placa-mãe de poeira; 5) Verificar se a bateria CMOS está funcionando; 6) Testar com fonte de alimentação conhecidamente funcional; 7) Considerar substituição da placa-mãe se o problema persistir.'),
    
    ({'bipes_1_longo_4_curto'}, 'Placa de vídeo não detectada (BIOS AMI). O sistema não consegue encontrar ou inicializar a placa de vídeo. Possíveis causas: placa não encaixada corretamente, defeito na placa, ou problema no slot. Soluções: 1) Verificar se a placa de vídeo está completamente encaixada no slot; 2) Verificar se os conectores de alimentação da placa estão conectados (se aplicável); 3) Limpar o slot PCIe/AGP; 4) Testar a placa em outro slot se disponível; 5) Testar com outra placa de vídeo; 6) Verificar se há atualização de BIOS disponível; 7) Considerar substituição da placa de vídeo.'),
    
    # Regras relacionadas a beeps da BIOS - Award
    ({'bipes_3_longos'}, 'Erro de memória RAM na memória principal (BIOS Award). Falha crítica na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Verificar se os módulos estão nos slots corretos; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória; 5) Testar com memória conhecidamente funcional; 6) Verificar configurações de memória no BIOS; 7) Considerar atualização do BIOS.'),
    
    ({'bipes_continuos'}, 'Problema na memória ou placa de vídeo (BIOS Award). Beeps contínuos indicam falha crítica. Possíveis causas: módulos de memória defeituosos, placa de vídeo com problema, ou incompatibilidade de componentes. Soluções: 1) Remover e testar módulos de memória individualmente; 2) Verificar se a placa de vídeo está bem encaixada; 3) Testar com outra placa de vídeo; 4) Limpar contatos de memória e placa de vídeo; 5) Verificar compatibilidade dos componentes; 6) Testar com componentes conhecidamente funcionais; 7) Verificar se há atualização de BIOS disponível.'),
    
    # Regras relacionadas a beeps da BIOS - Phoenix
    ({'bipes_1_1_1'}, 'Erro na CPU detectado (BIOS Phoenix - Código 1-1-1). Falha no processador durante o POST. Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. Soluções: 1) Verificar se o processador está bem encaixado no socket; 2) Verificar temperatura do processador e funcionamento do cooler; 3) Aplicar pasta térmica nova se necessário; 4) Verificar compatibilidade do processador com a placa-mãe; 5) Atualizar o BIOS para a versão mais recente; 6) Testar com outro processador compatível se possível; 7) Verificar se não há pinos dobrados no socket.'),
    
    ({'bipes_1_1_2'}, 'Erro na CPU detectado (BIOS Phoenix - Código 1-1-2). Falha no processador durante inicialização. Possíveis causas: CPU defeituosa, problema no cache do processador, ou incompatibilidade. Soluções: 1) Verificar encaixe do processador; 2) Verificar temperatura e cooler; 3) Verificar compatibilidade do processador; 4) Atualizar o BIOS; 5) Verificar configurações de CPU no BIOS; 6) Testar com outro processador compatível; 7) Considerar substituição do processador se o problema persistir.'),
    
    ({'bipes_1_1_3'}, 'Erro na CMOS detectado (BIOS Phoenix - Código 1-1-3). Problema com a memória de configuração do sistema. Possíveis causas: bateria CMOS descarregada, corrupção de dados CMOS, ou problema no chip CMOS. Soluções: 1) Substituir a bateria CMOS (tipo CR2032); 2) Limpar a CMOS (remover bateria por alguns minutos ou usar jumper CLR_CMOS); 3) Verificar se a bateria está bem encaixada; 4) Restaurar configurações padrão do BIOS após limpar CMOS; 5) Verificar se há atualização de BIOS disponível; 6) Se o problema persistir, pode indicar falha no chip CMOS da placa-mãe.'),
    
    ({'bipes_1_1_4'}, 'Erro no BIOS detectado (BIOS Phoenix - Código 1-1-4). Possível corrupção do firmware do BIOS. Possíveis causas: atualização de BIOS falha, corrupção de dados, ou falha no chip BIOS. Soluções: 1) Tentar restaurar o BIOS através de recuperação (se a placa-mãe suportar); 2) Verificar se há atualização de BIOS disponível; 3) Usar função de recuperação de BIOS da placa-mãe (se disponível); 4) Verificar se o chip BIOS está bem encaixado (se removível); 5) Contatar suporte do fabricante da placa-mãe; 6) Considerar substituição do chip BIOS ou da placa-mãe se necessário.'),
    
    ({'bipes_1_2_1'}, 'Erro no timer do sistema (BIOS Phoenix - Código 1-2-1). Falha no circuito de temporização da placa-mãe. Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. Soluções: 1) Desligar e desconectar da energia por alguns minutos; 2) Verificar se não há curto-circuito na placa-mãe; 3) Limpar a placa-mãe de poeira; 4) Verificar se todos os componentes estão bem conectados; 5) Verificar se a bateria CMOS está funcionando; 6) Considerar substituição da placa-mãe se o problema persistir.'),
    
    ({'bipes_1_2_2'}, 'Erro na DMA detectado (BIOS Phoenix - Código 1-2-2). Problema no controlador de acesso direto à memória. Possíveis causas: placa-mãe defeituosa, problema no chipset, ou conflito de hardware. Soluções: 1) Desligar e desconectar da energia; 2) Remover todos os componentes não essenciais; 3) Verificar se não há curto-circuito; 4) Limpar a placa-mãe; 5) Verificar se há atualização de BIOS disponível; 6) Testar com componentes mínimos (CPU, memória, vídeo); 7) Considerar substituição da placa-mãe se o problema persistir.'),
    
    ({'bipes_1_2_3'}, 'Erro na DMA detectado (BIOS Phoenix - Código 1-2-3). Falha no controlador de acesso direto à memória. Possíveis causas: placa-mãe defeituosa, problema no chipset, ou componente incompatível. Soluções: 1) Desligar e desconectar da energia; 2) Remover componentes não essenciais; 3) Verificar conexões de todos os componentes; 4) Limpar a placa-mãe; 5) Verificar compatibilidade dos componentes; 6) Atualizar o BIOS; 7) Considerar substituição da placa-mãe se necessário.'),
    
    ({'bipes_1_3_1'}, 'Erro na memória detectado (BIOS Phoenix - Código 1-3-1). Falha na memória RAM durante o POST. Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória; 5) Testar com módulos conhecidamente funcionais; 6) Verificar se os módulos estão nos slots corretos; 7) Verificar configurações de memória no BIOS.'),
    
    ({'bipes_1_3_3'}, 'Erro na memória detectado (BIOS Phoenix - Código 1-3-3). Falha na memória RAM durante inicialização. Possíveis causas: módulos defeituosos, problema na placa-mãe, ou configuração incorreta. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Limpar contatos dos módulos; 3) Verificar compatibilidade da memória com a placa-mãe; 4) Testar com memória conhecidamente funcional; 5) Verificar configurações de memória no BIOS; 6) Atualizar o BIOS; 7) Considerar substituição dos módulos se o problema persistir.'),
    
    # Regras relacionadas a beeps da BIOS - Dell
    ({'bipes_2_curtos'}, 'RAM não detectada (BIOS Dell). O sistema não consegue encontrar ou reconhecer os módulos de memória. Possíveis causas: módulos não encaixados corretamente, incompatibilidade, ou módulos defeituosos. Soluções: 1) Verificar se os módulos estão completamente encaixados; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória com a placa-mãe; 5) Consultar lista de memória compatível no site da Dell; 6) Testar com módulos conhecidamente funcionais; 7) Verificar se os módulos estão nos slots corretos conforme o manual.'),
    
    ({'bipes_3_curtos'}, 'Problema na placa-mãe detectado (BIOS Dell). Falha geral no sistema base. Possíveis causas: placa-mãe defeituosa, curto-circuito, ou componente mal conectado. Soluções: 1) Desligar e desconectar da energia; 2) Verificar se não há curto-circuito; 3) Remover e reinserir todos os componentes principais; 4) Limpar a placa-mãe de poeira; 5) Verificar bateria CMOS; 6) Testar com fonte de alimentação funcional; 7) Contatar suporte técnico da Dell; 8) Considerar substituição da placa-mãe se necessário.'),
    
    ({'bipes_4_curtos'}, 'Erro na memória RAM detectado (BIOS Dell). Falha na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória; 5) Consultar lista de memória compatível no site da Dell; 6) Testar com módulos conhecidamente funcionais; 7) Verificar configurações de memória no BIOS.'),
    
    ({'bipes_5_curtos'}, 'Problema no relógio em tempo real (RTC) detectado (BIOS Dell). Falha no circuito de relógio do sistema. Possíveis causas: bateria CMOS descarregada, problema no chip RTC, ou falha na placa-mãe. Soluções: 1) Substituir a bateria CMOS (tipo CR2032); 2) Verificar se a bateria está bem encaixada; 3) Limpar a CMOS (remover bateria por alguns minutos); 4) Verificar se há atualização de BIOS disponível; 5) Se o problema persistir, pode indicar falha no chip RTC da placa-mãe; 6) Contatar suporte técnico da Dell.'),
    
    ({'bipes_6_curtos'}, 'Erro no chipset da placa-mãe detectado (BIOS Dell). Falha no chipset principal ou secundário. Possíveis causas: chipset defeituoso, superaquecimento, ou problema na placa-mãe. Soluções: 1) Verificar temperatura do chipset; 2) Limpar poeira do dissipador do chipset; 3) Verificar se o dissipador está bem encaixado; 4) Desligar e desconectar da energia por alguns minutos; 5) Verificar se há atualização de BIOS disponível; 6) Contatar suporte técnico da Dell; 7) Considerar substituição da placa-mãe se o problema persistir.'),
    
    ({'bipes_7_curtos'}, 'Erro no processador detectado (BIOS Dell). Falha no CPU durante o POST. Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. Soluções: 1) Verificar se o processador está bem encaixado; 2) Verificar temperatura do processador e funcionamento do cooler; 3) Aplicar pasta térmica nova se necessário; 4) Verificar compatibilidade do processador; 5) Atualizar o BIOS; 6) Testar com outro processador compatível se possível; 7) Contatar suporte técnico da Dell.'),
    
    ({'bipes_8_curtos'}, 'Erro na placa de vídeo detectado (BIOS Dell). Falha na placa gráfica durante o POST. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar conectores de alimentação da placa (se aplicável); 3) Limpar o slot PCIe; 4) Testar com outra placa de vídeo; 5) Verificar temperatura da placa de vídeo; 6) Limpar poeira do cooler da placa; 7) Contatar suporte técnico da Dell; 8) Considerar substituição da placa de vídeo.'),
    
    # Regras relacionadas a beeps da BIOS - ASUS
    ({'bipes_1_longo'}, 'Problema na memória RAM detectado (BIOS ASUS). Falha na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória com a placa-mãe ASUS; 5) Consultar lista QVL (Qualified Vendor List) no site da ASUS; 6) Testar com módulos conhecidamente funcionais; 7) Verificar se os módulos estão nos slots corretos (geralmente slots A2/B2 para dual channel); 8) Verificar configurações de memória no BIOS.'),
    
    ({'bipes_1_longo_2_curtos'}, 'Erro na placa de vídeo detectado (BIOS ASUS). Falha na placa gráfica durante o POST. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot PCIe. Soluções: 1) Verificar se a placa de vídeo está completamente encaixada no slot PCIe; 2) Verificar conectores de alimentação PCIe (6/8 pinos); 3) Limpar o slot PCIe; 4) Testar em outro slot PCIe se disponível; 5) Testar com outra placa de vídeo; 6) Verificar temperatura da placa de vídeo; 7) Atualizar o BIOS da placa-mãe; 8) Considerar substituição da placa de vídeo.'),
    
    ({'bipes_1_longo_3_curtos'}, 'Erro na placa de vídeo detectado (BIOS ASUS). Falha na inicialização da placa gráfica. Possíveis causas: placa de vídeo defeituosa, problema na memória VRAM, ou incompatibilidade. Soluções: 1) Verificar encaixe da placa de vídeo; 2) Verificar conectores de alimentação; 3) Verificar temperatura e funcionamento do cooler; 4) Testar com outra placa de vídeo; 5) Limpar drivers antigos e instalar drivers atualizados; 6) Verificar compatibilidade da placa com a placa-mãe; 7) Atualizar o BIOS; 8) Considerar substituição da placa de vídeo.'),
    
    ({'bipes_continuos_curtos'}, 'Problema na memória RAM detectado (BIOS ASUS). Beeps curtos contínuos indicam falha crítica na memória. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Limpar contatos dos módulos; 3) Verificar compatibilidade no QVL da ASUS; 4) Testar com memória conhecidamente funcional; 5) Verificar se os módulos estão nos slots corretos; 6) Verificar configurações de memória no BIOS; 7) Atualizar o BIOS; 8) Considerar substituição dos módulos se necessário.'),
    
    # Regras relacionadas a beeps da BIOS - GIGABYTE
    ({'bipes_1_longo'}, 'Problema na memória RAM detectado (BIOS GIGABYTE). Falha na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória com a placa-mãe GIGABYTE; 5) Consultar lista de memória compatível no site da GIGABYTE; 6) Testar com módulos conhecidamente funcionais; 7) Verificar configurações de memória no BIOS; 8) Atualizar o BIOS se necessário.'),
    
    ({'bipes_1_longo_2_curtos'}, 'Erro na placa de vídeo detectado (BIOS GIGABYTE). Falha na placa gráfica durante o POST. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar conectores de alimentação PCIe; 3) Limpar o slot PCIe; 4) Testar com outra placa de vídeo; 5) Verificar temperatura da placa; 6) Atualizar o BIOS da placa-mãe; 7) Considerar substituição da placa de vídeo.'),
    
    ({'bipes_continuos_curtos'}, 'Problema na memória RAM detectado (BIOS GIGABYTE). Beeps curtos contínuos indicam falha crítica. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Limpar contatos dos módulos; 3) Verificar compatibilidade no site da GIGABYTE; 4) Testar com memória conhecidamente funcional; 5) Verificar slots de memória (geralmente slots 2 e 4 para dual channel); 6) Atualizar o BIOS; 7) Considerar substituição dos módulos.'),
    
    # Regras relacionadas a beeps da BIOS - MSI
    ({'bipes_1_longo'}, 'Problema na memória RAM detectado (BIOS MSI). Falha na memória do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. Soluções: 1) Remover e reinserir os módulos de memória; 2) Testar cada módulo individualmente; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória com a placa-mãe MSI; 5) Consultar lista de memória compatível no site da MSI; 6) Testar com módulos conhecidamente funcionais; 7) Verificar configurações de memória no BIOS; 8) Atualizar o BIOS se disponível.'),
    
    ({'bipes_1_longo_2_curtos'}, 'Erro na placa de vídeo detectado (BIOS MSI). Falha na placa gráfica durante o POST. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar conectores de alimentação PCIe; 3) Limpar o slot PCIe; 4) Testar com outra placa de vídeo; 5) Verificar temperatura da placa; 6) Atualizar o BIOS da placa-mãe; 7) Considerar substituição da placa de vídeo.'),
    
    ({'bipes_1_longo_3_curtos'}, 'Erro na placa de vídeo detectado (BIOS MSI). Falha na inicialização da placa gráfica. Possíveis causas: placa de vídeo defeituosa, problema na memória VRAM, ou incompatibilidade. Soluções: 1) Verificar encaixe da placa de vídeo; 2) Verificar conectores de alimentação; 3) Verificar temperatura e cooler; 4) Testar com outra placa de vídeo; 5) Limpar drivers e instalar drivers atualizados; 6) Verificar compatibilidade; 7) Atualizar o BIOS; 8) Considerar substituição da placa.'),
    
    ({'bipes_continuos_curtos'}, 'Problema na memória RAM detectado (BIOS MSI). Beeps curtos contínuos indicam falha crítica. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Limpar contatos dos módulos; 3) Verificar compatibilidade no site da MSI; 4) Testar com memória conhecidamente funcional; 5) Verificar slots de memória corretos; 6) Atualizar o BIOS; 7) Considerar substituição dos módulos.'),
    
    # Regras relacionadas a beeps da BIOS - HP/Compaq
    ({'bipes_3_curtos'}, 'Erro na memória base detectado (BIOS HP/Compaq). Falha na memória fundamental do sistema. Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. Soluções: 1) Remover todos os módulos e testar um por vez; 2) Verificar se os módulos estão nos slots corretos; 3) Limpar contatos dos módulos; 4) Verificar compatibilidade da memória; 5) Consultar especificações de memória no site da HP; 6) Testar com módulos conhecidamente funcionais; 7) Verificar configurações de memória no BIOS; 8) Considerar atualização do BIOS.'),
    
    ({'bipes_4_curtos'}, 'Timer do sistema falhou (BIOS HP/Compaq). Problema no circuito de temporização. Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. Soluções: 1) Desligar e desconectar da energia por alguns minutos; 2) Verificar se não há curto-circuito; 3) Limpar a placa-mãe de poeira; 4) Verificar se todos os componentes estão bem conectados; 5) Verificar bateria CMOS; 6) Contatar suporte técnico da HP; 7) Considerar substituição da placa-mãe se necessário.'),
    
    ({'bipes_5_curtos'}, 'Erro no processador detectado (BIOS HP/Compaq). Falha no CPU durante o POST. Possíveis causas: CPU defeituosa, superaquecimento, ou conexão incorreta. Soluções: 1) Verificar se o processador está bem encaixado; 2) Verificar temperatura do processador e funcionamento do cooler; 3) Aplicar pasta térmica nova se necessário; 4) Verificar compatibilidade do processador; 5) Atualizar o BIOS; 6) Contatar suporte técnico da HP; 7) Considerar substituição do processador se necessário.'),
    
    ({'bipes_1_longo_2_curtos'}, 'Erro na placa de vídeo detectado (BIOS HP/Compaq). Falha na placa gráfica durante o POST. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar conectores de alimentação se aplicável; 3) Limpar o slot PCIe; 4) Testar com outra placa de vídeo; 5) Verificar temperatura da placa; 6) Contatar suporte técnico da HP; 7) Considerar substituição da placa de vídeo.'),
    
    # Regras relacionadas a beeps genéricos
    ({'bipes_continuos_curtos'}, 'Problema crítico na fonte de alimentação ou placa-mãe. Beeps curtos contínuos indicam falha grave no sistema. Possíveis causas: fonte de alimentação defeituosa, placa-mãe com problema, curto-circuito, ou componente queimado. Soluções: 1) Desligar imediatamente e desconectar da energia; 2) Verificar se não há curto-circuito visível; 3) Testar com outra fonte de alimentação conhecidamente funcional; 4) Verificar se todos os conectores estão bem encaixados; 5) Remover componentes não essenciais e testar; 6) Verificar se há componentes queimados ou com cheiro de queimado; 7) Limpar a placa-mãe de poeira; 8) Considerar substituição da fonte ou placa-mãe se necessário.'),
    
    ({'sem_bipes'}, 'Possível problema na fonte de alimentação ou placa-mãe. Ausência de beeps indica que o sistema não está completando o POST. Possíveis causas: fonte de alimentação defeituosa, placa-mãe com problema, CPU não funcionando, ou curto-circuito. Soluções: 1) Verificar se a fonte está ligada e funcionando (testar com multímetro se possível); 2) Verificar se o botão de ligar está funcionando; 3) Testar com outra fonte de alimentação; 4) Verificar se o processador está bem encaixado; 5) Verificar se não há curto-circuito; 6) Remover todos os componentes não essenciais e testar; 7) Verificar se há componentes queimados; 8) Considerar substituição da fonte ou placa-mãe se necessário.'),
    
    # Regras relacionadas a problemas de vídeo
    ({'sem_video', 'bipes_continuos'}, 'Possível defeito na GPU ou placa de vídeo. Combinação de ausência de vídeo e beeps contínuos indica falha crítica na placa gráfica. Possíveis causas: placa de vídeo queimada, problema na memória VRAM, superaquecimento, ou incompatibilidade. Soluções: 1) Verificar se a placa de vídeo está bem encaixada; 2) Verificar conectores de alimentação da placa; 3) Verificar temperatura da placa de vídeo; 4) Limpar poeira do cooler da placa; 5) Testar com outra placa de vídeo; 6) Testar o monitor em outro computador; 7) Verificar se o cabo de vídeo está funcionando; 8) Considerar substituição da placa de vídeo.'),
    
    ({'sem_video', 'bipes_1_longo_2_curto'}, 'Falha na placa de vídeo confirmada. Erro de vídeo combinado com ausência de sinal indica problema na placa gráfica. Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. Soluções: 1) Verificar se a placa está completamente encaixada no slot; 2) Verificar conectores de alimentação PCIe; 3) Limpar o slot PCIe e contatos da placa; 4) Testar a placa em outro slot se disponível; 5) Testar com outra placa de vídeo; 6) Verificar se o monitor está funcionando; 7) Testar com outro cabo de vídeo; 8) Considerar substituição da placa de vídeo.'),
    
    ({'sem_video', 'bipes_continuos_curtos'}, 'Problema na placa de vídeo ou fonte de alimentação. Combinação indica possível falha de energia na placa gráfica ou defeito na mesma. Possíveis causas: fonte de alimentação insuficiente, placa de vídeo defeituosa, ou problema nos conectores de alimentação. Soluções: 1) Verificar se a fonte tem potência suficiente para a placa de vídeo; 2) Verificar conectores de alimentação PCIe (6/8 pinos); 3) Testar com outra fonte de alimentação mais potente; 4) Verificar se a placa de vídeo está bem encaixada; 5) Testar com outra placa de vídeo; 6) Verificar temperatura da placa; 7) Considerar substituição da fonte ou placa de vídeo.'),
    
    # Regras relacionadas a problemas de hardware crítico
    ({'nao_liga', 'cheiro_queimado'}, 'CRÍTICO: Possível curto-circuito na placa-mãe ou componente queimado. DESLIGUE IMEDIATAMENTE E DESCONECTE DA ENERGIA. Presença de cheiro de queimado indica dano físico grave. Possíveis causas: componente queimado, curto-circuito, ou sobrecarga elétrica. Ações imediatas: 1) DESLIGAR e DESCONECTAR da energia IMEDIATAMENTE; 2) NÃO tentar ligar novamente até identificar o problema; 3) Inspecionar visualmente componentes queimados (capacitores inchados, marcas de queimado); 4) Verificar se há componentes soltos ou em contato indevido; 5) Verificar fonte de alimentação (pode ter causado o problema); 6) NÃO usar o equipamento até reparo profissional; 7) Considerar substituição de componentes afetados ou da placa-mãe inteira.'),
    
    ({'reiniciando', 'superaquecimento'}, 'Falha no sistema de refrigeração detectada. Reinicializações constantes combinadas com superaquecimento indicam problema crítico de temperatura. Possíveis causas: cooler do processador não funcionando, pasta térmica seca, dissipador solto, ou fluxo de ar insuficiente. Soluções: 1) Verificar se o cooler do processador está funcionando (girando); 2) Verificar temperatura do processador no BIOS ou software de monitoramento; 3) Limpar poeira do cooler e dissipador; 4) Aplicar pasta térmica nova; 5) Verificar se o dissipador está bem encaixado; 6) Verificar fluxo de ar do gabinete (ventiladores funcionando); 7) Considerar substituição do cooler se necessário; 8) Verificar se há overclock que possa estar causando superaquecimento.'),
    
    ({'tela_azul', 'reiniciando'}, 'Possível problema de driver ou memória RAM instável. Tela azul (BSOD) combinada com reinicializações indica falha de software ou hardware instável. Possíveis causas: driver corrompido, memória RAM defeituosa, ou problema no sistema operacional. Soluções: 1) Verificar código de erro da tela azul (anotar código de erro); 2) Testar memória RAM com ferramenta de diagnóstico (MemTest86); 3) Atualizar drivers, especialmente de vídeo e chipset; 4) Verificar se há atualizações do Windows disponíveis; 5) Verificar temperatura dos componentes; 6) Desfazer overclock se houver; 7) Verificar se há arquivos corrompidos no sistema; 8) Considerar restauração do sistema ou reinstalação do SO se necessário.'),
    
    ({'lento', 'superaquecimento'}, 'Sistema em throttling térmico. Desempenho reduzido devido a proteção contra superaquecimento. O processador está reduzindo sua velocidade para evitar danos. Possíveis causas: cooler insuficiente, pasta térmica seca, ou fluxo de ar inadequado. Soluções: 1) Verificar temperatura do processador (deve estar abaixo de 80°C em carga); 2) Limpar poeira do cooler e dissipador; 3) Aplicar pasta térmica nova de qualidade; 4) Verificar se o cooler está funcionando corretamente; 5) Melhorar fluxo de ar do gabinete (adicionar ventiladores se necessário); 6) Verificar se o dissipador está bem encaixado; 7) Considerar upgrade do cooler se o atual for insuficiente; 8) Verificar se há overclock excessivo.'),
    
    ({'travando', 'superaquecimento'}, 'Sistema travando devido a superaquecimento crítico. Travamentos combinados com alta temperatura indicam falha grave na refrigeração. Possíveis causas: cooler não funcionando, dissipador solto, ou fluxo de ar completamente bloqueado. Soluções: 1) DESLIGAR o sistema imediatamente para evitar danos permanentes; 2) Verificar se o cooler do processador está girando; 3) Verificar temperatura crítica (pode estar acima de 90°C); 4) Limpar toda poeira do sistema de refrigeração; 5) Aplicar pasta térmica nova; 6) Verificar se o dissipador está firmemente encaixado; 7) Verificar fluxo de ar do gabinete; 8) Substituir o cooler se não estiver funcionando; 9) Considerar upgrade do sistema de refrigeração.'),
    
    ({'ruido_estranho', 'superaquecimento'}, 'Possível falha no cooler detectada. Ruído estranho combinado com superaquecimento indica problema no sistema de refrigeração. Possíveis causas: cooler com rolamento defeituoso, cooler parado, ou obstrução no fluxo de ar. Soluções: 1) Identificar a origem do ruído (qual cooler está fazendo barulho); 2) Verificar se o cooler está girando; 3) Limpar poeira e obstruções; 4) Verificar se o cooler está bem encaixado; 5) Aplicar óleo nos rolamentos se for possível (coolers antigos); 6) Substituir o cooler defeituoso; 7) Verificar temperatura dos componentes; 8) Melhorar fluxo de ar do gabinete; 9) Considerar substituição preventiva de outros coolers se forem antigos.')
]

