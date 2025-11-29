from baseDeRegras import REGRAS, extrair_fatos_da_conclusao

class MotorInferencia:
    def __init__(self, regras=None):
        self.regras = regras if regras is not None else REGRAS
        self.max_iteracoes = 100
    
    def encad_tras(self, fatos):
        fatos = set(fatos)
        conclusoes = []
        justificativas = []
        
        for condicoes, conclusao in self.regras:
            if condicoes.issubset(fatos):
                conclusoes.append(conclusao)
                fatos_ativadores = ', '.join(sorted(condicoes))
                justificativas.append(
                    f"Regra ativada por: [{fatos_ativadores}] → {conclusao}"
                )
        
        # Retorna resultado
        if conclusoes:
            return {
                'conclusoes': conclusoes,
                'justificativas': justificativas,
                'fatos_usados': list(fatos)
            }
        else:
            return {
                'conclusoes': ["Nenhuma conclusão encontrada com os fatos fornecidos"],
                'justificativas': ["Nenhuma regra foi ativada com os fatos informados"],
                'fatos_usados': list(fatos)
            }
    
    def obter_regras(self):
        return self.regras
    
    def contar_regras(self):
        return len(self.regras)
    
    def encad_frente(self, fatos):
        fatos_conhecidos = set(fatos)
        fatos_iniciais = set(fatos) 
        fatos_derivados = set()  
        conclusoes = []  
        justificativas = []  
        arvore_deducao = [] 
        regras_ativadas = set()  # Para evitar processar a mesma regra múltiplas vezes
        
        iteracao = 0
        mudou = True 
        
        # Algoritmo de forward chaining 
        while mudou and iteracao < self.max_iteracoes:
            mudou = False
            iteracao += 1
            
            # Verifica cada regra
            for idx, (condicoes, conclusao) in enumerate(self.regras):
                if idx in regras_ativadas:
                    continue
                
                if condicoes.issubset(fatos_conhecidos):
                    if conclusao not in conclusoes:
                        conclusoes.append(conclusao)
                        
                        # Cria justificativa
                        fatos_ativadores = ', '.join(sorted(condicoes))
                        justificativa = f"Regra ativada por: [{fatos_ativadores}] → {conclusao}"
                        justificativas.append(justificativa)
                        
                        arvore_deducao.append({
                            'fatos_necessarios': sorted(condicoes),
                            'conclusao': conclusao,
                            'iteracao': iteracao
                        })
                        
                        mudou = True
                        regras_ativadas.add(idx)
                        
                        fatos_extraidos = extrair_fatos_da_conclusao(conclusao)
                        for fato_extraido in fatos_extraidos:
                            if fato_extraido not in fatos_conhecidos:
                                fatos_conhecidos.add(fato_extraido)
                                fatos_derivados.add(fato_extraido)
                                mudou = True
                                
                                arvore_deducao.append({
                                    'fatos_necessarios': [conclusao],
                                    'conclusao': f"Fato derivado: {fato_extraido}",
                                    'iteracao': iteracao,
                                    'tipo': 'fato_derivado'
                                })
        
        # Retorna resultado
        if conclusoes:
            return {
                'conclusoes': conclusoes,
                'justificativas': justificativas,
                'fatos_usados': list(fatos_conhecidos),
                'fatos_iniciais': list(fatos_iniciais),
                'fatos_derivados': list(fatos_derivados),
                'arvore_deducao': arvore_deducao,
                'iteracoes': iteracao
            }
        else:
            return {
                'conclusoes': ["Nenhuma conclusão encontrada com os fatos fornecidos"],
                'justificativas': ["Nenhuma regra foi ativada com os fatos informados"],
                'fatos_usados': list(fatos_conhecidos),
                'fatos_iniciais': list(fatos_iniciais),
                'fatos_derivados': list(fatos_derivados),
                'arvore_deducao': [],
                'iteracoes': iteracao
            }
    
    def encad_hibrido(self, fatos):
        resultado_backward = self.encad_tras(fatos)
        
        fatos_para_forward = set(fatos)
        
        for conclusao in resultado_backward['conclusoes']:
            fatos_extraidos = extrair_fatos_da_conclusao(conclusao)
            fatos_para_forward.update(fatos_extraidos)
        
        resultado_forward = self.encad_frente(list(fatos_para_forward))
        
        # Combina resultados
        conclusoes_combinadas = resultado_backward['conclusoes'] + resultado_forward['conclusoes']
        conclusoes_unicas = []
        for c in conclusoes_combinadas:
            if c not in conclusoes_unicas:
                conclusoes_unicas.append(c)
        
        justificativas_combinadas = resultado_backward['justificativas'] + resultado_forward['justificativas']
        
        return {
            'conclusoes': conclusoes_unicas,
            'justificativas': justificativas_combinadas,
            'fatos_usados': list(set(resultado_backward['fatos_usados'] + resultado_forward.get('fatos_usados', []))),
            'fatos_iniciais': list(fatos),
            'fatos_derivados': resultado_forward.get('fatos_derivados', []),
            'arvore_deducao': resultado_forward.get('arvore_deducao', []),
            'metodo': 'hibrido',
            'backward': resultado_backward,
            'forward': resultado_forward
        }

