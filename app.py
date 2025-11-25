
from flask import Flask, render_template, request, jsonify
from motorInferencia import MotorInferencia
from baseDeRegras import FABRICANTES_BIOS, BIPES_POR_FABRICANTE, OUTROS_ERROS, obter_bipes_fabricante
import re

app = Flask(__name__)
motor = MotorInferencia()

def formatar_diagnostico(texto):
    """
    Formata o texto do diagnóstico para exibição mais legível
    Quebra em parágrafos, formata listas e destaca seções importantes
    """
    if not texto:
        return texto
    
    # Verifica se é mensagem crítica (cheiro de queimado)
    is_critico = 'CRÍTICO' in texto.upper() or 'DESLIGUE IMEDIATAMENTE' in texto.upper()
    
    # Separa o texto em seções principais
    partes_formatadas = []
    
    # Identifica e formata seções
    if 'Possíveis causas:' in texto:
        partes = texto.split('Possíveis causas:', 1)
        # Descrição inicial
        descricao = partes[0].strip()
        if descricao:
            classe_paragrafo = 'mb-3 text-danger fw-bold' if is_critico else 'mb-3'
            partes_formatadas.append(f'<p class="{classe_paragrafo}">{descricao}</p>')
        
        if len(partes) > 1:
            resto = partes[1]
            if 'Soluções:' in resto or 'Ações imediatas:' in resto:
                # Usa 'Ações imediatas:' se existir, senão 'Soluções:'
                separador = 'Ações imediatas:' if 'Ações imediatas:' in resto else 'Soluções:'
                causas_solucoes = resto.split(separador, 1)
                # Formata causas
                causas = causas_solucoes[0].strip()
                if causas:
                    partes_formatadas.append('<p class="fw-bold text-warning mb-2">⚠️ Possíveis causas:</p>')
                    partes_formatadas.append(f'<p class="mb-3 ms-3">{causas}</p>')
                
                # Formata soluções/ações
                if len(causas_solucoes) > 1:
                    solucoes = causas_solucoes[1].strip()
                    if solucoes:
                        label = '🚨 Ações imediatas:' if 'Ações imediatas:' in resto else '✅ Soluções:'
                        classe_label = 'fw-bold text-danger mb-2' if is_critico else 'fw-bold text-success mb-2'
                        partes_formatadas.append(f'<p class="{classe_label}">{label}</p>')
                        # Formata lista numerada
                        solucoes_formatadas = formatar_lista_numerada(solucoes)
                        partes_formatadas.append(f'<div class="ms-3">{solucoes_formatadas}</div>')
            else:
                causas = resto.strip()
                if causas:
                    partes_formatadas.append('<p class="fw-bold text-warning mb-2">⚠️ Possíveis causas:</p>')
                    partes_formatadas.append(f'<p class="mb-3 ms-3">{causas}</p>')
    elif 'Soluções:' in texto or 'Ações imediatas:' in texto:
        separador = 'Ações imediatas:' if 'Ações imediatas:' in texto else 'Soluções:'
        partes = texto.split(separador, 1)
        descricao = partes[0].strip()
        if descricao:
            classe_paragrafo = 'mb-3 text-danger fw-bold' if is_critico else 'mb-3'
            partes_formatadas.append(f'<p class="{classe_paragrafo}">{descricao}</p>')
        if len(partes) > 1:
            solucoes = partes[1].strip()
            if solucoes:
                label = '🚨 Ações imediatas:' if 'Ações imediatas:' in texto else '✅ Soluções:'
                classe_label = 'fw-bold text-danger mb-2' if is_critico else 'fw-bold text-success mb-2'
                partes_formatadas.append(f'<p class="{classe_label}">{label}</p>')
                solucoes_formatadas = formatar_lista_numerada(solucoes)
                partes_formatadas.append(f'<div class="ms-3">{solucoes_formatadas}</div>')
    else:
        # Se não tem seções específicas, apenas quebra em parágrafos
        classe_paragrafo = 'mb-2 text-danger fw-bold' if is_critico else 'mb-2'
        partes_formatadas.append(f'<p class="{classe_paragrafo}">{texto}</p>')
    
    return ''.join(partes_formatadas)

def formatar_lista_numerada(texto):
    """
    Formata uma lista numerada (ex: "1) item 2) item") em HTML
    """
    import re
    # Padrão melhorado para identificar itens numerados
    # Captura: número) seguido de conteúdo até o próximo número) ou fim
    padrao = r'(\d+)\)\s*([^0-9]+?)(?=\s*\d+\)|$)'
    itens = re.findall(padrao, texto, re.DOTALL)
    
    if itens and len(itens) > 0:
        html_lista = '<ol class="mb-0 lista-solucoes">'
        for num, conteudo in itens:
            # Limpa o conteúdo: remove espaços extras e pontuação final desnecessária
            conteudo_limpo = conteudo.strip()
            # Remove ponto final se estiver sozinho no final (mas mantém se fizer parte do texto)
            if conteudo_limpo.endswith('.') and len(conteudo_limpo) > 1:
                # Verifica se não é uma abreviação comum
                if not any(abrev in conteudo_limpo[-3:] for abrev in ['etc.', 'ex.', 'i.e.', 'e.g.']):
                    conteudo_limpo = conteudo_limpo.rstrip('.')
            html_lista += f'<li class="mb-2">{conteudo_limpo}</li>'
        html_lista += '</ol>'
        return html_lista
    else:
        # Se não encontrar padrão numerado, retorna o texto formatado em parágrafo
        return f'<p class="mb-0">{texto}</p>'

def formatar_nome_fato(fato):
    """
    Formata o nome do fato para exibição mais legível
    Ex: 'bipes_1_longo_2_curto' -> 'Beeps: 1 longo, 2 curtos'
    """
    if fato.startswith('bipes_'):
        # Remove o prefixo 'bipes_'
        resto = fato[6:]
        
        # Casos especiais
        if resto == 'continuos':
            return 'Beeps: contínuos'
        elif resto == 'continuos_curtos':
            return 'Beeps: curtos contínuos'
        elif resto == '1_curto':
            return 'Beeps: 1 curto'
        elif resto == '1_longo':
            return 'Beeps: 1 longo'
        elif resto == 'sem_bipes':
            return 'Sem beeps'
        
        # Padrão: números e palavras separadas por underscore
        partes = resto.split('_')
        
        # Verifica se é padrão Phoenix (1_1_1, 1_1_2, etc.)
        if len(partes) >= 3 and all(p.isdigit() for p in partes):
            return f"Beeps: {'-'.join(partes)}"
        
        # Processa padrão normal: número + tipo
        resultado = []
        i = 0
        while i < len(partes):
            if partes[i].isdigit():
                # É um número, pega o próximo como tipo
                if i + 1 < len(partes):
                    tipo = partes[i + 1]
                    if tipo == 'longo':
                        resultado.append(f"{partes[i]} longo")
                    elif tipo == 'curto' or tipo == 'curtos':
                        resultado.append(f"{partes[i]} curto" if partes[i] == '1' else f"{partes[i]} curtos")
                    else:
                        resultado.append(f"{partes[i]} {tipo}")
                    i += 2
                else:
                    resultado.append(partes[i])
                    i += 1
            else:
                resultado.append(partes[i])
                i += 1
        
        if resultado:
            return 'Beeps: ' + ', '.join(resultado)
        else:
            return 'Beeps: ' + resto.replace('_', ' ')
    
    # Para outros erros, apenas formata melhor
    return fato.replace('_', ' ').title()

@app.route("/", methods=["GET", "POST"])
def index():
    diagnostico = None
    fatos_selecionados = []
    fabricante_selecionado = None
    metodo_inferencia = None
    
    if request.method == "POST":
        # Obtém o fabricante selecionado
        fabricante_selecionado = request.form.get("fabricante", "")
        
        # Obtém o método de inferência selecionado (padrão: backward)
        metodo_inferencia = request.form.get("metodo_inferencia", "backward")
        
        # Obtém todos os checkboxes selecionados
        fatos = request.form.getlist("fatos")
        fatos = [f.strip() for f in fatos if f.strip()]
        fatos_selecionados = fatos
        
        if fatos:
            # Aplica o método de inferência selecionado
            if metodo_inferencia == "forward":
                resultado = motor.encad_frente(fatos)
            elif metodo_inferencia == "hibrido":
                resultado = motor.encad_hibrido(fatos)
            else:  # backward (padrão)
                resultado = motor.encad_tras(fatos)
            
            # Formata cada diagnóstico para exibição
            diagnosticos_formatados = []
            for d in resultado['conclusoes']:
                formato_html = formatar_diagnostico(d)
                diagnosticos_formatados.append({
                    'html': formato_html,
                    'texto_original': d,
                    'is_critico': 'CRÍTICO' in d.upper() or 'DESLIGUE IMEDIATAMENTE' in d.upper()
                })
            
            # Adiciona informações adicionais do resultado (para forward e híbrido)
            diagnostico = {
                'diagnosticos': diagnosticos_formatados,
                'metodo': metodo_inferencia,
                'justificativas': resultado.get('justificativas', []),
                'fatos_iniciais': resultado.get('fatos_iniciais', fatos),
                'fatos_derivados': resultado.get('fatos_derivados', []),
                'arvore_deducao': resultado.get('arvore_deducao', []),
                'iteracoes': resultado.get('iteracoes', 0)
            }
        else:
            diagnostico = {
                'diagnosticos': [{'html': 'Por favor, selecione pelo menos um fato para diagnóstico.', 'texto_original': '', 'is_critico': False}],
                'metodo': metodo_inferencia or 'backward',
                'justificativas': [],
                'fatos_iniciais': [],
                'fatos_derivados': [],
                'arvore_deducao': [],
                'iteracoes': 0
            }
    
    # Obtém os beeps do fabricante selecionado ou todos se nenhum foi selecionado
    if fabricante_selecionado and fabricante_selecionado in BIPES_POR_FABRICANTE:
        bipes_disponiveis = BIPES_POR_FABRICANTE[fabricante_selecionado]
    else:
        # Se nenhum fabricante selecionado, mostra beeps genéricos
        bipes_disponiveis = BIPES_POR_FABRICANTE.get('desconhecido', {})
    
    # Formata os fatos selecionados para exibição
    fatos_formatados = [formatar_nome_fato(f) for f in fatos_selecionados] if fatos_selecionados else []
    
    return render_template(
        "index.html", 
        diagnostico=diagnostico, 
        bipes_disponiveis=bipes_disponiveis,
        outros_erros=OUTROS_ERROS,
        fabricantes=FABRICANTES_BIOS,
        fabricante_selecionado=fabricante_selecionado,
        fatos_selecionados=fatos_selecionados,
        fatos_formatados=fatos_formatados,
        metodo_inferencia=metodo_inferencia or 'backward',
        formatar_nome_fato=formatar_nome_fato
    )

@app.route("/api/bipes/<fabricante>")
def api_bipes(fabricante):
    """API endpoint para obter beeps de um fabricante específico"""
    bipes = obter_bipes_fabricante(fabricante)
    return jsonify(bipes)

if __name__ == "__main__":
    app.run(debug=True)
