def gerar_justificativa(resultado, fatos_iniciais):
    """Gera justificativa formatada das inferências"""
    if not resultado.get('conclusoes'):
        return "Nenhuma regra foi ativada com os fatos fornecidos."
    
    justificativa = []
    justificativa.append(f"**Fatos informados:** {', '.join(fatos_iniciais)}")
    
    if resultado.get('justificativas'):
        justificativa.append("\n**Regras ativadas:**")
        for i, just in enumerate(resultado['justificativas'], 1):
            justificativa.append(f"{i}. {just}")
    
    if resultado.get('fatos_derivados'):
        justificativa.append(f"\n**Fatos derivados:** {', '.join(resultado['fatos_derivados'])}")
    
    if resultado.get('iteracoes'):
        justificativa.append(f"\n**Iterações:** {resultado['iteracoes']}")
    
    return '\n'.join(justificativa)

def formatar_justificativa_html(resultado, fatos_iniciais, formatar_fato=None):
    """Gera justificativa formatada em HTML"""
    if not resultado.get('conclusoes'):
        return "<p>Nenhuma regra foi ativada com os fatos fornecidos.</p>"
    
    formatar = formatar_fato if formatar_fato else lambda x: x.replace('_', ' ').title()
    
    html = []
    fatos_formatados = [formatar(f) for f in fatos_iniciais]
    html.append(f'<p class="mb-2"><strong>Fatos informados:</strong> {", ".join(fatos_formatados)}</p>')
    
    if resultado.get('justificativas'):
        html.append('<p class="mb-2"><strong>Regras ativadas:</strong></p>')
        html.append('<ol class="ms-3">')
        for just in resultado['justificativas']:
            html.append(f'<li class="mb-1">{just}</li>')
        html.append('</ol>')
    
    if resultado.get('fatos_derivados'):
        fatos_derivados_formatados = [formatar(f) for f in resultado['fatos_derivados']]
        html.append(f'<p class="mb-2"><strong>Fatos derivados:</strong> {", ".join(fatos_derivados_formatados)}</p>')
    
    if resultado.get('iteracoes'):
        html.append(f'<p class="mb-0"><strong>Iterações:</strong> {resultado["iteracoes"]}</p>')
    
    return ''.join(html)
