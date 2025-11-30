
function filtrarBipes() {
    const fabricante = document.getElementById('fabricanteSelect').value;
    const bipesContainer = document.getElementById('bipesContainer');
    
    if (fabricante) {
        // Faz requisição AJAX para obter beeps do fabricante
        fetch(`/api/bipes/${fabricante}`)
            .then(response => response.json())
            .then(data => {
                const form = document.getElementById('diagnosticoForm');
                const existingBipes = form.querySelectorAll('input[name="fatos"][id^="fato_"]');
                existingBipes.forEach(cb => {
                    const label = document.querySelector(`label[for="${cb.id}"]`);
                    if (label && label.closest('.bipes-container')) {
                        cb.closest('.col-md-6').remove();
                    }
                });
                
                const bipesDiv = bipesContainer.querySelector('.row') || document.createElement('div');
                if (!bipesContainer.querySelector('.row')) {
                    bipesDiv.className = 'row';
                    bipesContainer.appendChild(bipesDiv);
                }
                
                let index = 1;
                for (const [fato, descricao] of Object.entries(data)) {
                    const col = document.createElement('div');
                    col.className = 'col-md-6 mb-2';
                    const fatoFormatado = formatarNomeFato(fato);
                    col.innerHTML = `
                        <div class="d-flex align-items-center">
                            <div class="form-check flex-grow-1">
                                <input class="form-check-input" type="checkbox" name="fatos" value="${fato}" id="fato_${index}">
                                <label class="form-check-label" for="fato_${index}">
                                    <strong>${fatoFormatado}</strong>
                                </label>
                            </div>
                            <button type="button" class="btn btn-sm btn-outline-secondary ms-2 flex-shrink-0" onclick="tocarBeep('${fato}')" title="Ouvir beep">
                                Ouvir
                            </button>
                        </div>
                    `;
                    bipesDiv.appendChild(col);
                    index++;
                }
                
                bipesContainer.classList.add('show');
            })
            .catch(error => {
                console.error('Erro ao carregar beeps:', error);
                bipesContainer.classList.remove('show');
            });
    } else {
        bipesContainer.classList.remove('show');
    }
}


function formatarNomeFato(fato) {
    if (fato.startsWith('bipes_')) {
        const resto = fato.substring(6);
        
        if (resto === 'continuos') return 'Beeps: contínuos';
        if (resto === 'continuos_curtos') return 'Beeps: curtos contínuos';
        if (resto === '1_curto') return 'Beeps: 1 curto';
        if (resto === '1_longo') return 'Beeps: 1 longo';
        if (resto === 'sem_bipes') return 'Sem beeps';
        
        const partes = resto.split('_');
        
        if (partes.length >= 3 && partes.every(p => /^\d+$/.test(p))) {
            return `Beeps: ${partes.join('-')}`;
        }
        
        const resultado = [];
        let i = 0;
        
        while (i < partes.length) {
            if (/^\d+$/.test(partes[i])) {
                if (i + 1 < partes.length) {
                    const tipo = partes[i + 1];
                    if (tipo === 'longo') {
                        resultado.push(`${partes[i]} longo`);
                    } else if (tipo === 'curto' || tipo === 'curtos') {
                        resultado.push(partes[i] === '1' ? `${partes[i]} curto` : `${partes[i]} curtos`);
                    } else {
                        resultado.push(`${partes[i]} ${tipo}`);
                    }
                    i += 2;
                } else {
                    resultado.push(partes[i]);
                    i++;
                }
            } else {
                resultado.push(partes[i]);
                i++;
            }
        }
        
        if (resultado.length > 0) {
            return 'Beeps: ' + resultado.join(', ');
        } else {
            return 'Beeps: ' + resto.replace(/_/g, ' ');
        }
    }
    
    return fato.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
}

const beepPlayer = new BeepPlayer();


async function tocarBeep(fato) {
    await beepPlayer.tocarBeep(fato);
}

document.addEventListener('DOMContentLoaded', function() {

    const fabricanteSelect = document.getElementById('fabricanteSelect');
    if (fabricanteSelect) {
        fabricanteSelect.addEventListener('change', filtrarBipes);
        
        const fabricante = fabricanteSelect.value;
        if (fabricante) {
            filtrarBipes();
        }
    }
});

