from flask import Flask, render_template, request, jsonify
from core.inference.motor_inferencia import MotorInferencia
from core.domain.dados import FABRICANTES_BIOS, BIPES_POR_FABRICANTE, OUTROS_ERROS, obter_bipes_fabricante
from core.utils.justificativa import formatar_justificativa_html
import re
import os

app = Flask(__name__)
motor = MotorInferencia()

def formatar_diagnostico(texto, is_critico=False):
    if not texto:
        return texto
    
    partes_formatadas = []
    if 'Possíveis causas:' in texto:
        partes = texto.split('Possíveis causas:', 1)
        descricao = partes[0].strip()
        if descricao:
            classe_paragrafo = 'mb-3 text-danger fw-bold' if is_critico else 'mb-3'
            partes_formatadas.append(f'<p class="{classe_paragrafo}">{descricao}</p>')
        
        if len(partes) > 1:
            resto = partes[1]
            if 'Soluções:' in resto or 'Ações imediatas:' in resto:
                separador = 'Ações imediatas:' if 'Ações imediatas:' in resto else 'Soluções:'
                causas_solucoes = resto.split(separador, 1)
                causas = causas_solucoes[0].strip()
                if causas:
                    partes_formatadas.append('<p class="fw-bold text-warning mb-2">Possíveis causas:</p>')
                    partes_formatadas.append(f'<p class="mb-3 ms-3">{causas}</p>')
                
                if len(causas_solucoes) > 1:
                    solucoes = causas_solucoes[1].strip()
                    if solucoes:
                        label = 'Ações imediatas:' if 'Ações imediatas:' in resto else 'Soluções:'
                        classe_label = 'fw-bold text-danger mb-2' if is_critico else 'fw-bold text-success mb-2'
                        partes_formatadas.append(f'<p class="{classe_label}">{label}</p>')
                        solucoes_formatadas = formatar_lista_numerada(solucoes)
                        partes_formatadas.append(f'<div class="ms-3">{solucoes_formatadas}</div>')
            else:
                causas = resto.strip()
                if causas:
                    partes_formatadas.append('<p class="fw-bold text-warning mb-2">Possíveis causas:</p>')
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
                label = 'Ações imediatas:' if 'Ações imediatas:' in texto else 'Soluções:'
                classe_label = 'fw-bold text-danger mb-2' if is_critico else 'fw-bold text-success mb-2'
                partes_formatadas.append(f'<p class="{classe_label}">{label}</p>')
                solucoes_formatadas = formatar_lista_numerada(solucoes)
                partes_formatadas.append(f'<div class="ms-3">{solucoes_formatadas}</div>')
    else:
        classe_paragrafo = 'mb-2 text-danger fw-bold' if is_critico else 'mb-2'
        partes_formatadas.append(f'<p class="{classe_paragrafo}">{texto}</p>')
    
    return ''.join(partes_formatadas)

def formatar_lista_numerada(texto):
    padrao = r'(\d+)\)\s*([^0-9]+?)(?=\s*\d+\)|$)'
    itens = re.findall(padrao, texto, re.DOTALL)
    
    if itens:
        html_lista = '<ol class="mb-0 lista-solucoes">'
        for num, conteudo in itens:
            conteudo_limpo = conteudo.strip()
            if conteudo_limpo.endswith('.') and len(conteudo_limpo) > 1:
                if not any(abrev in conteudo_limpo[-3:] for abrev in ['etc.', 'ex.', 'i.e.', 'e.g.']):
                    conteudo_limpo = conteudo_limpo.rstrip('.')
            html_lista += f'<li class="mb-2">{conteudo_limpo}</li>'
        html_lista += '</ol>'
        return html_lista
    else:
        return f'<p class="mb-0">{texto}</p>'

def formatar_nome_fato(fato):
    if fato.startswith('bipes_'):
        resto = fato[6:]
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
        
        partes = resto.split('_')
        if len(partes) >= 3 and all(p.isdigit() for p in partes):
            return f"Beeps: {'-'.join(partes)}"
        
        resultado = []
        i = 0
        while i < len(partes):
            if partes[i].isdigit():
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
        fatos = [f.strip() for f in request.form.getlist("fatos") if f.strip()]
        fatos_selecionados = fatos
        
        if fatos:
            # Aplica o método de inferência selecionado
            if metodo_inferencia == "forward":
                resultado = motor.encad_frente(fatos)
            elif metodo_inferencia == "hibrido":
                resultado = motor.encad_hibrido(fatos)
            else:  
                resultado = motor.encad_tras(fatos)
            
            # Formata cada diagnóstico para exibição
            diagnosticos_formatados = []
            for d in resultado['conclusoes']:
                is_critico = 'CRÍTICO' in d.upper() or 'DESLIGUE IMEDIATAMENTE' in d.upper()
                formato_html = formatar_diagnostico(d, is_critico)
                diagnosticos_formatados.append({
                    'html': formato_html,
                    'texto_original': d,
                    'is_critico': is_critico
                })
            
            fatos_iniciais = resultado.get('fatos_iniciais', fatos)
            diagnostico = {
                'diagnosticos': diagnosticos_formatados,
                'metodo': metodo_inferencia,
                'justificativas': resultado.get('justificativas', []),
                'justificativa_html': formatar_justificativa_html(resultado, fatos_iniciais, formatar_nome_fato),
                'fatos_iniciais': fatos_iniciais,
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
    
    bipes_disponiveis = BIPES_POR_FABRICANTE.get(fabricante_selecionado if fabricante_selecionado in BIPES_POR_FABRICANTE else 'desconhecido', {})
    
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
