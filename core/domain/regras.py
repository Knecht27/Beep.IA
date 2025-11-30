"""Regras de diagnóstico do sistema especialista"""

REGRAS = [
    # REGRAS RELACIONADAS A BEEPS DA BIOS - AMI
    (
        {'bipes_1_curto'},
        'POST bem-sucedido - Sistema funcionando normalmente. '
        'O computador passou por todos os testes de inicialização sem erros. '
        'Nenhuma ação necessária.'
    ),
    (
        {'bipes_1_longo_2_curto'},
        'Erro de vídeo detectado (BIOS AMI). '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, monitor sem sinal, ou problema no slot PCIe/AGP. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Testar com outra placa de vídeo; '
        '3) Verificar conexão do cabo de vídeo.'
    ),
    (
        {'bipes_1_longo_3_curto'},
        'Erro de memória RAM detectado (BIOS AMI). '
        'Possíveis causas: módulos de memória defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos com borracha.'
    ),
    (
        {'bipes_2_curtos'},
        'Erro de paridade na memória RAM. '
        'Indica falha na verificação de integridade dos dados na memória. '
        'Possíveis causas: módulo de memória defeituoso, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover módulos de memória e testar um por vez; '
        '2) Verificar se a memória é compatível com a placa-mãe; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_3_curtos'},
        'Erro nos primeiros 64KB de memória (BIOS AMI). '
        'Falha crítica na memória base do sistema. '
        'Possíveis causas: módulo de memória defeituoso, problema na placa-mãe, ou configuração incorreta. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Verificar se os módulos estão no slot correto (geralmente slot 1); '
        '3) Limpar contatos dos módulos.'
    ),
    (
        {'bipes_4_curtos'},
        'Timer do sistema falhou (BIOS AMI). '
        'Problema no circuito de temporização da placa-mãe. '
        'Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. '
        'Soluções: 1) Desligar o computador e desconectar da energia por alguns minutos; '
        '2) Verificar se não há curto-circuito na placa-mãe; '
        '3) Limpar a placa-mãe de poeira.'
    ),
    (
        {'bipes_5_curtos'},
        'Erro no processador detectado (BIOS AMI). '
        'Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. '
        'Soluções: 1) Verificar se o processador está bem encaixado no socket; '
        '2) Verificar temperatura do processador; '
        '3) Verificar se o cooler está funcionando corretamente.'
    ),
    (
        {'bipes_6_curtos'},
        'Erro no controlador de teclado (BIOS AMI). '
        'Problema na comunicação com o teclado durante o POST. '
        'Possíveis causas: teclado defeituoso, conexão solta, ou problema na placa-mãe. '
        'Soluções: 1) Desconectar e reconectar o teclado; '
        '2) Testar com outro teclado; '
        '3) Verificar se o teclado está conectado na porta correta (PS/2 ou USB).'
    ),
    
    (
        {'bipes_7_curtos'},
        'Erro no modo virtual (BIOS AMI). '
        'Falha no processador ao entrar em modo de processamento virtual. '
        'Possíveis causas: CPU defeituosa, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Verificar se o processador está bem encaixado; '
        '2) Verificar compatibilidade do processador; '
        '3) Atualizar o BIOS para a versão mais recente.'
    ),
    
    (
        {'bipes_8_curtos'},
        'Erro na memória de vídeo (BIOS AMI). '
        'Problema na memória dedicada da placa de vídeo. '
        'Possíveis causas: placa de vídeo defeituosa, memória VRAM corrompida, ou superaquecimento. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar temperatura da placa de vídeo; '
        '3) Limpar poeira do cooler da placa de vídeo.'
    ),
    (
        {'bipes_1_longo'},
        'Erro de memória RAM detectado. '
        'Falha geral na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir todos os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos com borracha.'
    ),
    (
        {'bipes_1_longo_1_curto'},
        'Problema na placa-mãe detectado (BIOS AMI). '
        'Falha geral no sistema base. '
        'Possíveis causas: placa-mãe defeituosa, curto-circuito, ou componente mal conectado. '
        'Soluções: 1) Desligar e desconectar da energia; '
        '2) Verificar se não há curto-circuito (parafusos soltos, componentes em contato); '
        '3) Remover e reinserir todos os componentes principais.'
    ),
    (
        {'bipes_1_longo_4_curto'},
        'Placa de vídeo não detectada (BIOS AMI). '
        'O sistema não consegue encontrar ou inicializar a placa de vídeo. '
        'Possíveis causas: placa não encaixada corretamente, defeito na placa, ou problema no slot. '
        'Soluções: 1) Verificar se a placa de vídeo está completamente encaixada no slot; '
        '2) Verificar se os conectores de alimentação da placa estão conectados (se aplicável); '
        '3) Limpar o slot PCIe/AGP.'
    ),

    # REGRAS RELACIONADAS A BEEPS DA BIOS - AWARD
    (
        {'bipes_3_longos'},
        'Erro de memória RAM na memória principal (BIOS Award). '
        'Falha crítica na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Verificar se os módulos estão nos slots corretos; '
        '3) Limpar contatos dos módulos.'
    ),
    (
        {'bipes_continuos'},
        'Problema na memória ou placa de vídeo (BIOS Award). '
        'Beeps contínuos indicam falha crítica. '
        'Possíveis causas: módulos de memória defeituosos, placa de vídeo com problema, ou incompatibilidade de componentes. '
        'Soluções: 1) Remover e testar módulos de memória individualmente; '
        '2) Verificar se a placa de vídeo está bem encaixada; '
        '3) Testar com outra placa de vídeo.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - PHOENIX
    (
        {'bipes_1_1_1'},
        'Erro na CPU detectado (BIOS Phoenix - Código 1-1-1). '
        'Falha no processador durante o POST. '
        'Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. '
        'Soluções: 1) Verificar se o processador está bem encaixado no socket; '
        '2) Verificar temperatura do processador e funcionamento do cooler; '
        '3) Aplicar pasta térmica nova se necessário.'
    ),
    (
        {'bipes_1_1_2'},
        'Erro na CPU detectado (BIOS Phoenix - Código 1-1-2). '
        'Falha no processador durante inicialização. '
        'Possíveis causas: CPU defeituosa, problema no cache do processador, ou incompatibilidade. '
        'Soluções: 1) Verificar encaixe do processador; '
        '2) Verificar temperatura e cooler; '
        '3) Verificar compatibilidade do processador.'
    ),
    
    (
        {'bipes_1_1_3'},
        'Erro na CMOS detectado (BIOS Phoenix - Código 1-1-3). '
        'Problema com a memória de configuração do sistema. '
        'Possíveis causas: bateria CMOS descarregada, corrupção de dados CMOS, ou problema no chip CMOS. '
        'Soluções: 1) Substituir a bateria CMOS (tipo CR2032); '
        '2) Limpar a CMOS (remover bateria por alguns minutos ou usar jumper CLR_CMOS); '
        '3) Verificar se a bateria está bem encaixada.'
    ),
    
    (
        {'bipes_1_1_4'},
        'Erro no BIOS detectado (BIOS Phoenix - Código 1-1-4). '
        'Possível corrupção do firmware do BIOS. '
        'Possíveis causas: atualização de BIOS falha, corrupção de dados, ou falha no chip BIOS. '
        'Soluções: 1) Tentar restaurar o BIOS através de recuperação (se a placa-mãe suportar); '
        '2) Verificar se há atualização de BIOS disponível; '
        '3) Usar função de recuperação de BIOS da placa-mãe (se disponível).'
    ),
    
    (
        {'bipes_1_2_1'},
        'Erro no timer do sistema (BIOS Phoenix - Código 1-2-1). '
        'Falha no circuito de temporização da placa-mãe. '
        'Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. '
        'Soluções: 1) Desligar e desconectar da energia por alguns minutos; '
        '2) Verificar se não há curto-circuito na placa-mãe; '
        '3) Limpar a placa-mãe de poeira.'
    ),
    
    (
        {'bipes_1_2_2'},
        'Erro na DMA detectado (BIOS Phoenix - Código 1-2-2). '
        'Problema no controlador de acesso direto à memória. '
        'Possíveis causas: placa-mãe defeituosa, problema no chipset, ou conflito de hardware. '
        'Soluções: 1) Desligar e desconectar da energia; '
        '2) Remover todos os componentes não essenciais; '
        '3) Verificar se não há curto-circuito.'
    ),
    
    (
        {'bipes_1_2_3'},
        'Erro na DMA detectado (BIOS Phoenix - Código 1-2-3). '
        'Falha no controlador de acesso direto à memória. '
        'Possíveis causas: placa-mãe defeituosa, problema no chipset, ou componente incompatível. '
        'Soluções: 1) Desligar e desconectar da energia; '
        '2) Remover componentes não essenciais; '
        '3) Verificar conexões de todos os componentes.'
    ),
    
    (
        {'bipes_1_3_1'},
        'Erro na memória detectado (BIOS Phoenix - Código 1-3-1). '
        'Falha na memória RAM durante o POST. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_1_3_3'},
        'Erro na memória detectado (BIOS Phoenix - Código 1-3-3). '
        'Falha na memória RAM durante inicialização. '
        'Possíveis causas: módulos defeituosos, problema na placa-mãe, ou configuração incorreta. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Limpar contatos dos módulos; '
        '3) Verificar compatibilidade da memória com a placa-mãe.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - DELL
    
    (
        {'bipes_2_curtos'},
        'RAM não detectada (BIOS Dell). '
        'O sistema não consegue encontrar ou reconhecer os módulos de memória. '
        'Possíveis causas: módulos não encaixados corretamente, incompatibilidade, ou módulos defeituosos. '
        'Soluções: 1) Verificar se os módulos estão completamente encaixados; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_3_curtos'},
        'Problema na placa-mãe detectado (BIOS Dell). '
        'Falha geral no sistema base. '
        'Possíveis causas: placa-mãe defeituosa, curto-circuito, ou componente mal conectado. '
        'Soluções: 1) Desligar e desconectar da energia; '
        '2) Verificar se não há curto-circuito; '
        '3) Remover e reinserir todos os componentes principais.'
    ),
    
    (
        {'bipes_4_curtos'},
        'Erro na memória RAM detectado (BIOS Dell). '
        'Falha na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_5_curtos'},
        'Problema no relógio em tempo real (RTC) detectado (BIOS Dell). '
        'Falha no circuito de relógio do sistema. '
        'Possíveis causas: bateria CMOS descarregada, problema no chip RTC, ou falha na placa-mãe. '
        'Soluções: 1) Substituir a bateria CMOS (tipo CR2032); '
        '2) Verificar se a bateria está bem encaixada; '
        '3) Limpar a CMOS (remover bateria por alguns minutos).'
    ),
    
    (
        {'bipes_6_curtos'},
        'Erro no chipset da placa-mãe detectado (BIOS Dell). '
        'Falha no chipset principal ou secundário. '
        'Possíveis causas: chipset defeituoso, superaquecimento, ou problema na placa-mãe. '
        'Soluções: 1) Verificar temperatura do chipset; '
        '2) Limpar poeira do dissipador do chipset; '
        '3) Verificar se o dissipador está bem encaixado.'
    ),
    
    (
        {'bipes_7_curtos'},
        'Erro no processador detectado (BIOS Dell). '
        'Falha no CPU durante o POST. '
        'Possíveis causas: CPU defeituosa, superaquecimento, conexão incorreta, ou incompatibilidade. '
        'Soluções: 1) Verificar se o processador está bem encaixado; '
        '2) Verificar temperatura do processador e funcionamento do cooler; '
        '3) Aplicar pasta térmica nova se necessário.'
    ),
    
    (
        {'bipes_8_curtos'},
        'Erro na placa de vídeo detectado (BIOS Dell). '
        'Falha na placa gráfica durante o POST. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar conectores de alimentação da placa (se aplicável); '
        '3) Limpar o slot PCIe.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - ASUS
    
    (
        {'bipes_1_longo'},
        'Problema na memória RAM detectado (BIOS ASUS). '
        'Falha na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_1_longo_2_curtos'},
        'Erro na placa de vídeo detectado (BIOS ASUS). '
        'Falha na placa gráfica durante o POST. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot PCIe. '
        'Soluções: 1) Verificar se a placa de vídeo está completamente encaixada no slot PCIe; '
        '2) Verificar conectores de alimentação PCIe (6/8 pinos); '
        '3) Limpar o slot PCIe.'
    ),
    
    (
        {'bipes_1_longo_3_curtos'},
        'Erro na placa de vídeo detectado (BIOS ASUS). '
        'Falha na inicialização da placa gráfica. '
        'Possíveis causas: placa de vídeo defeituosa, problema na memória VRAM, ou incompatibilidade. '
        'Soluções: 1) Verificar encaixe da placa de vídeo; '
        '2) Verificar conectores de alimentação; '
        '3) Verificar temperatura e funcionamento do cooler.'
    ),
    
    (
        {'bipes_continuos_curtos'},
        'Problema na memória RAM detectado (BIOS ASUS). '
        'Beeps curtos contínuos indicam falha crítica na memória. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Limpar contatos dos módulos; '
        '3) Verificar compatibilidade no QVL da ASUS.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - GIGABYTE
    
    (
        {'bipes_1_longo'},
        'Problema na memória RAM detectado (BIOS GIGABYTE). '
        'Falha na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_1_longo_2_curtos'},
        'Erro na placa de vídeo detectado (BIOS GIGABYTE). '
        'Falha na placa gráfica durante o POST. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar conectores de alimentação PCIe; '
        '3) Limpar o slot PCIe.'
    ),
    
    (
        {'bipes_continuos_curtos'},
        'Problema na memória RAM detectado (BIOS GIGABYTE). '
        'Beeps curtos contínuos indicam falha crítica. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Limpar contatos dos módulos; '
        '3) Verificar compatibilidade no site da GIGABYTE.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - MSI

    
    (
        {'bipes_1_longo'},
        'Problema na memória RAM detectado (BIOS MSI). '
        'Falha na memória do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou encaixe incorreto. '
        'Soluções: 1) Remover e reinserir os módulos de memória; '
        '2) Testar cada módulo individualmente; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_1_longo_2_curtos'},
        'Erro na placa de vídeo detectado (BIOS MSI). '
        'Falha na placa gráfica durante o POST. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar conectores de alimentação PCIe; '
        '3) Limpar o slot PCIe.'
    ),
    
    (
        {'bipes_1_longo_3_curtos'},
        'Erro na placa de vídeo detectado (BIOS MSI). '
        'Falha na inicialização da placa gráfica. '
        'Possíveis causas: placa de vídeo defeituosa, problema na memória VRAM, ou incompatibilidade. '
        'Soluções: 1) Verificar encaixe da placa de vídeo; '
        '2) Verificar conectores de alimentação; '
        '3) Verificar temperatura e cooler.'
    ),
    
    (
        {'bipes_continuos_curtos'},
        'Problema na memória RAM detectado (BIOS MSI). '
        'Beeps curtos contínuos indicam falha crítica. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Limpar contatos dos módulos; '
        '3) Verificar compatibilidade no site da MSI.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS DA BIOS - HP/COMPAQ

    (
        {'bipes_3_curtos'},
        'Erro na memória base detectado (BIOS HP/Compaq). '
        'Falha na memória fundamental do sistema. '
        'Possíveis causas: módulos defeituosos, incompatibilidade, ou problema na placa-mãe. '
        'Soluções: 1) Remover todos os módulos e testar um por vez; '
        '2) Verificar se os módulos estão nos slots corretos; '
        '3) Limpar contatos dos módulos.'
    ),
    
    (
        {'bipes_4_curtos'},
        'Timer do sistema falhou (BIOS HP/Compaq). '
        'Problema no circuito de temporização. '
        'Possíveis causas: placa-mãe defeituosa, problema no chipset, ou falha no cristal oscilador. '
        'Soluções: 1) Desligar e desconectar da energia por alguns minutos; '
        '2) Verificar se não há curto-circuito; '
        '3) Limpar a placa-mãe de poeira.'
    ),
    
    (
        {'bipes_5_curtos'},
        'Erro no processador detectado (BIOS HP/Compaq). '
        'Falha no CPU durante o POST. '
        'Possíveis causas: CPU defeituosa, superaquecimento, ou conexão incorreta. '
        'Soluções: 1) Verificar se o processador está bem encaixado; '
        '2) Verificar temperatura do processador e funcionamento do cooler; '
        '3) Aplicar pasta térmica nova se necessário.'
    ),
    
    (
        {'bipes_1_longo_2_curtos'},
        'Erro na placa de vídeo detectado (BIOS HP/Compaq). '
        'Falha na placa gráfica durante o POST. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar conectores de alimentação se aplicável; '
        '3) Limpar o slot PCIe.'
    ),
    
    # REGRAS RELACIONADAS A BEEPS GENÉRICOS
    
    (
        {'bipes_continuos_curtos'},
        'Problema crítico na fonte de alimentação ou placa-mãe. '
        'Beeps curtos contínuos indicam falha grave no sistema. '
        'Possíveis causas: fonte de alimentação defeituosa, placa-mãe com problema, curto-circuito, ou componente queimado. '
        'Soluções: 1) Desligar imediatamente e desconectar da energia; '
        '2) Verificar se não há curto-circuito visível; '
        '3) Testar com outra fonte de alimentação conhecidamente funcional.'
    ),
    
    (
        {'sem_bipes'},
        'Possível problema na fonte de alimentação ou placa-mãe. '
        'Ausência de beeps indica que o sistema não está completando o POST. '
        'Possíveis causas: fonte de alimentação defeituosa, placa-mãe com problema, CPU não funcionando, ou curto-circuito. '
        'Soluções: 1) Verificar se a fonte está ligada e funcionando (testar com multímetro se possível); '
        '2) Verificar se o botão de ligar está funcionando; '
        '3) Testar com outra fonte de alimentação.'
    ),
    
    # REGRAS RELACIONADAS A PROBLEMAS DE VÍDEO
    
    (
        {'sem_video', 'bipes_continuos'},
        'Possível defeito na GPU ou placa de vídeo. '
        'Combinação de ausência de vídeo e beeps contínuos indica falha crítica na placa gráfica. '
        'Possíveis causas: placa de vídeo queimada, problema na memória VRAM, superaquecimento, ou incompatibilidade. '
        'Soluções: 1) Verificar se a placa de vídeo está bem encaixada; '
        '2) Verificar conectores de alimentação da placa; '
        '3) Verificar temperatura da placa de vídeo.'
    ),
    
    (
        {'sem_video', 'bipes_1_longo_2_curto'},
        'Falha na placa de vídeo confirmada. '
        'Erro de vídeo combinado com ausência de sinal indica problema na placa gráfica. '
        'Possíveis causas: placa de vídeo defeituosa, conexão solta, ou problema no slot. '
        'Soluções: 1) Verificar se a placa está completamente encaixada no slot; '
        '2) Verificar conectores de alimentação PCIe; '
        '3) Limpar o slot PCIe e contatos da placa.'
    ),
    
    (
        {'sem_video', 'bipes_continuos_curtos'},
        'Problema na placa de vídeo ou fonte de alimentação. '
        'Combinação indica possível falha de energia na placa gráfica ou defeito na mesma. '
        'Possíveis causas: fonte de alimentação insuficiente, placa de vídeo defeituosa, ou problema nos conectores de alimentação. '
        'Soluções: 1) Verificar se a fonte tem potência suficiente para a placa de vídeo; '
        '2) Verificar conectores de alimentação PCIe (6/8 pinos); '
        '3) Testar com outra fonte de alimentação mais potente.'
    ),
    
    # REGRAS RELACIONADAS A PROBLEMAS DE HARDWARE CRÍTICO
    
    (
        {'nao_liga', 'cheiro_queimado'},
        'CRÍTICO: Possível curto-circuito na placa-mãe ou componente queimado. '
        'DESLIGUE IMEDIATAMENTE E DESCONECTE DA ENERGIA. '
        'Presença de cheiro de queimado indica dano físico grave. '
        'Possíveis causas: componente queimado, curto-circuito, ou sobrecarga elétrica. '
        'Ações imediatas: 1) DESLIGAR e DESCONECTAR da energia IMEDIATAMENTE; '
        '2) NÃO tentar ligar novamente até identificar o problema; '
        '3) Inspecionar visualmente componentes queimados (capacitores inchados, marcas de queimado).'
    ),
    
    (
        {'reiniciando', 'superaquecimento'},
        'Falha no sistema de refrigeração detectada. '
        'Reinicializações constantes combinadas com superaquecimento indicam problema crítico de temperatura. '
        'Possíveis causas: cooler do processador não funcionando, pasta térmica seca, dissipador solto, ou fluxo de ar insuficiente. '
        'Soluções: 1) Verificar se o cooler do processador está funcionando (girando); '
        '2) Verificar temperatura do processador no BIOS ou software de monitoramento; '
        '3) Limpar poeira do cooler e dissipador.'
    ),
    
    (
        {'tela_azul', 'reiniciando'},
        'Possível problema de driver ou memória RAM instável. '
        'Tela azul (BSOD) combinada com reinicializações indica falha de software ou hardware instável. '
        'Possíveis causas: driver corrompido, memória RAM defeituosa, ou problema no sistema operacional. '
        'Soluções: 1) Verificar código de erro da tela azul (anotar código de erro); '
        '2) Testar memória RAM com ferramenta de diagnóstico (MemTest86); '
        '3) Atualizar drivers, especialmente de vídeo e chipset.'
    ),
    
    (
        {'lento', 'superaquecimento'},
        'Sistema em throttling térmico. '
        'Desempenho reduzido devido a proteção contra superaquecimento. '
        'O processador está reduzindo sua velocidade para evitar danos. '
        'Possíveis causas: cooler insuficiente, pasta térmica seca, ou fluxo de ar inadequado. '
        'Soluções: 1) Verificar temperatura do processador (deve estar abaixo de 80°C em carga); '
        '2) Limpar poeira do cooler e dissipador; '
        '3) Aplicar pasta térmica nova de qualidade.'
    ),
    
    (
        {'travando', 'superaquecimento'},
        'Sistema travando devido a superaquecimento crítico. '
        'Travamentos combinados com alta temperatura indicam falha grave na refrigeração. '
        'Possíveis causas: cooler não funcionando, dissipador solto, ou fluxo de ar completamente bloqueado. '
        'Soluções: 1) DESLIGAR o sistema imediatamente para evitar danos permanentes; '
        '2) Verificar se o cooler do processador está girando; '
        '3) Verificar temperatura crítica (pode estar acima de 90°C).'
    ),
    
    (
        {'ruido_estranho', 'superaquecimento'},
        'Possível falha no cooler detectada. '
        'Ruído estranho combinado com superaquecimento indica problema no sistema de refrigeração. '
        'Possíveis causas: cooler com rolamento defeituoso, cooler parado, ou obstrução no fluxo de ar. '
        'Soluções: 1) Identificar a origem do ruído (qual cooler está fazendo barulho); '
        '2) Verificar se o cooler está girando; '
        '3) Limpar poeira e obstruções.'
    )
]

