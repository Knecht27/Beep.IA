
class BeepPlayer {

    constructor() {
        this.frequenciaPadrao = 1000; 
        this.volumePadrao = 0.08;
    }


    gerarBeep(frequencia = this.frequenciaPadrao, duracao = 200) {
        return new Promise((resolve) => {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            const filter = audioContext.createBiquadFilter();
            
            oscillator.connect(filter);
            filter.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = frequencia;
            oscillator.type = 'sawtooth';
            
            filter.type = 'lowpass';
            filter.frequency.value = 2000;
            filter.Q.value = 1;
            
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

    async reproduzirBeepsContinuos(quantidade = 8, duracaoBeep = 250, intervalo = 150) {
        for (let i = 0; i < quantidade; i++) {
            await this.gerarBeep(this.frequenciaPadrao, duracaoBeep);
            if (i < quantidade - 1) {
                await this.aguardar(intervalo);
            }
        }
    }


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
            
            // Pausa longa entre grupos 
            if (i < sequencia.length - 1) {
                await this.aguardar(300);
            }
        }
    }

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


    processarFato(resto) {

        if (resto === 'sem_bipes') {
            return null; // Sem beeps
        }
        
        if (resto === 'continuos') {
            return { tipo: 'continuos', quantidade: 8, duracao: 250, intervalo: 150 };
        }
        
        if (resto === 'continuos_curtos') {
            return { tipo: 'continuos_curtos', quantidade: 10, duracao: 150, intervalo: 200 };
        }
        

        const partes = resto.split('_');
        if (partes.length >= 3 && partes.every(p => /^\d+$/.test(p))) {
            return { tipo: 'phoenix', sequencia: partes.map(p => parseInt(p)) };
        }
        
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

    async tocarBeep(fato) {
        if (!fato.startsWith('bipes_')) {
            return; // Não é um beep
        }
        
        const resto = fato.substring(6);
        const processado = this.processarFato(resto);
        
        if (!processado) {
            return; 
        }
        
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

    aguardar(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

