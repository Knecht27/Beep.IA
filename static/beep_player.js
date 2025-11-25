/**
 * Classe responsável por gerenciar a reprodução de beeps de BIOS
 * Utiliza Web Audio API para gerar sons similares aos beeps reais de POST
 */
class BeepPlayer {
    /**
     * Construtor da classe BeepPlayer
     */
    constructor() {
        this.frequenciaPadrao = 1000; // Frequência típica de beeps de BIOS POST (1000 Hz)
        this.volumePadrao = 0.08; // Volume baixo para não incomodar
    }

    /**
     * Gera um beep usando Web Audio API (similar a beeps reais de BIOS POST)
     * @param {number} frequencia - Frequência do beep em Hz (padrão: 1000Hz)
     * @param {number} duracao - Duração do beep em milissegundos (padrão: 200ms)
     * @returns {Promise} Promise que resolve quando o beep termina
     */
    gerarBeep(frequencia = this.frequenciaPadrao, duracao = 200) {
        return new Promise((resolve) => {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            const filter = audioContext.createBiquadFilter();
            
            // Conecta: oscillator -> filter -> gain -> destination
            oscillator.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            // Configuração do oscilador
            oscillator.frequency.value = frequencia;
            oscillator.type = 'sawtooth'; // Timbre brilhante e metálico (como buzzer de BIOS)
            
            // Filtro passa-baixa para suavizar o timbre
            filter.type = 'lowpass';
            filter.frequency.value = 2000; // Frequência de corte que suaviza mas mantém o caráter metálico
            filter.Q.value = 1;
            
            // Envelope de volume
            gainNode.gain.setValueAtTime(this.volumePadrao, audioContext.currentTime);
            gainNode.gain.linearRampToValueAtTime(this.volumePadrao, audioContext.currentTime + (duracao * 0.85) / 1000);
            gainNode.gain.linearRampToValueAtTime(0.01, audioContext.currentTime + duracao / 1000);
            
            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + duracao / 1000);
            
            oscillator.onended = () => {
                resolve();
            };
        });
    }

    /**
     * Reproduz beeps contínuos
     * @param {number} quantidade - Número de beeps a reproduzir
     * @param {number} duracaoBeep - Duração de cada beep em ms
     * @param {number} intervalo - Intervalo entre beeps em ms
     * @returns {Promise} Promise que resolve quando todos os beeps terminam
     */
    async reproduzirBeepsContinuos(quantidade = 8, duracaoBeep = 250, intervalo = 150) {
        for (let i = 0; i < quantidade; i++) {
            await this.gerarBeep(this.frequenciaPadrao, duracaoBeep);
            if (i < quantidade - 1) {
                await this.aguardar(intervalo);
            }
        }
    }

    /**
     * Reproduz sequência Phoenix (ex: 1-1-1, 1-1-2, etc.)
     * @param {Array<number>} sequencia - Array com números da sequência Phoenix
     * @returns {Promise} Promise que resolve quando a sequência termina
     */
    async reproduzirSequenciaPhoenix(sequencia) {
        for (let i = 0; i < sequencia.length; i++) {
            const quantidade = sequencia[i];
            
            // Reproduz os beeps do grupo
            for (let j = 0; j < quantidade; j++) {
                await this.gerarBeep(this.frequenciaPadrao, 100);
                if (j < quantidade - 1) {
                    await this.aguardar(50); // Pausa curta entre beeps do mesmo grupo
                }
            }
            
            // Pausa longa entre grupos (exceto no último)
            if (i < sequencia.length - 1) {
                await this.aguardar(300);
            }
        }
    }

    /**
     * Reproduz uma sequência de beeps baseada no tipo (curto/longo)
     * @param {Array<Object>} sequencias - Array de objetos {quantidade, tipo}
     * @returns {Promise} Promise que resolve quando todas as sequências terminam
     */
    async reproduzirSequencias(sequencias) {
        for (let seqIdx = 0; seqIdx < sequencias.length; seqIdx++) {
            const { quantidade, tipo } = sequencias[seqIdx];
            
            for (let j = 0; j < quantidade; j++) {
                const duracao = tipo === 'longo' ? 500 : 200;
                await this.gerarBeep(this.frequenciaPadrao, duracao);
                
                // Pausa entre beeps do mesmo tipo
                if (j < quantidade - 1) {
                    await this.aguardar(150);
                }
            }
            
            // Pausa entre sequências diferentes
            if (seqIdx < sequencias.length - 1) {
                await this.aguardar(500);
            }
        }
    }

    /**
     * Processa o nome do fato e extrai sequências de beeps
     * @param {string} resto - Parte do nome do fato após "bipes_"
     * @returns {Array<Object>|Array<number>|null} Sequências processadas ou null se não for beep válido
     */
    processarFato(resto) {
        // Casos especiais
        if (resto === 'sem_bipes') {
            return null; // Sem beeps
        }
        
        if (resto === 'continuos') {
            return { tipo: 'continuos', quantidade: 8, duracao: 250, intervalo: 150 };
        }
        
        if (resto === 'continuos_curtos') {
            return { tipo: 'continuos_curtos', quantidade: 10, duracao: 150, intervalo: 200 };
        }
        
        // Padrão Phoenix (1_1_1, 1_1_2, etc.)
        const partes = resto.split('_');
        if (partes.length >= 3 && partes.every(p => /^\d+$/.test(p))) {
            return { tipo: 'phoenix', sequencia: partes.map(p => parseInt(p)) };
        }
        
        // Processa padrão normal: número + tipo (ex: 1_curto, 2_curtos, 1_longo, 1_longo_2_curto)
        const sequencias = [];
        let i = 0;
        
        while (i < partes.length) {
            if (/^\d+$/.test(partes[i])) {
                const quantidade = parseInt(partes[i]);
                let tipo = 'curto';
                
                // Verifica se há um tipo após o número
                if (i + 1 < partes.length) {
                    const proximaParte = partes[i + 1];
                    if (proximaParte === 'longo' || proximaParte === 'curto' || proximaParte === 'curtos') {
                        tipo = proximaParte;
                        i += 2;
                    } else {
                        i += 1;
                    }
                } else {
                    i += 1;
                }
                
                sequencias.push({ quantidade, tipo });
            } else {
                i++;
            }
        }
        
        if (sequencias.length > 0) {
            return { tipo: 'sequencias', sequencias };
        }
        
        return null;
    }

    /**
     * Reproduz uma sequência de beeps baseado no tipo de beep
     * @param {string} fato - Nome do fato/beep a ser reproduzido
     * @returns {Promise} Promise que resolve quando o beep termina
     */
    async tocarBeep(fato) {
        if (!fato.startsWith('bipes_')) {
            return; // Não é um beep
        }
        
        const resto = fato.substring(6);
        const processado = this.processarFato(resto);
        
        if (!processado) {
            return; // Sem beeps ou inválido
        }
        
        // Reproduz baseado no tipo processado
        switch (processado.tipo) {
            case 'continuos':
                await this.reproduzirBeepsContinuos(processado.quantidade, processado.duracao, processado.intervalo);
                break;
                
            case 'continuos_curtos':
                await this.reproduzirBeepsContinuos(processado.quantidade, processado.duracao, processado.intervalo);
                break;
                
            case 'phoenix':
                await this.reproduzirSequenciaPhoenix(processado.sequencia);
                break;
                
            case 'sequencias':
                await this.reproduzirSequencias(processado.sequencias);
                break;
        }
    }

    /**
     * Utilitário para aguardar um tempo em milissegundos
     * @param {number} ms - Tempo em milissegundos
     * @returns {Promise} Promise que resolve após o tempo especificado
     */
    aguardar(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

