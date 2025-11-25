"""
Motor de Inferência - Sistema Especialista
Implementa os mecanismos de encadeamento para trás (backward chaining)
e encadeamento para frente (forward chaining) para processar regras e fatos
e gerar conclusões
"""

from baseDeRegras import REGRAS, extrair_fatos_da_conclusao


class MotorInferencia:
    """
    Motor de inferência que aplica encadeamento para trás e para frente
    para diagnosticar problemas baseado em fatos fornecidos
    """
    
    def __init__(self, regras=None):
        """
        Inicializa o motor de inferência
        
        Args:
            regras: Lista de regras (opcional, usa REGRAS da base de conhecimento por padrão)
        """
        self.regras = regras if regras is not None else REGRAS
        self.max_iteracoes = 100  # Limite de iterações para evitar loops infinitos
    
    def encad_tras(self, fatos):
        """
        Aplica encadeamento para trás (backward chaining)
        
        Args:
            fatos: Lista ou conjunto de fatos observados
            
        Returns:
            Lista de conclusões encontradas baseadas nas regras aplicáveis
        """
        fatos = set(fatos)
        conclusoes = []
        justificativas = []
        
        # Verifica cada regra
        for condicoes, conclusao in self.regras:
            # Se todas as condições da regra estão presentes nos fatos
            if condicoes.issubset(fatos):
                conclusoes.append(conclusao)
                # Cria justificativa mostrando quais fatos ativaram a regra
                fatos_ativadores = ', '.join(sorted(condicoes))
                justificativas.append(
                    f"Regra ativada por: [{fatos_ativadores}] → {conclusao}"
                )
        
        # Retorna resultado ou mensagem padrão
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
        """
        Retorna todas as regras do sistema
        
        Returns:
            Lista de tuplas (condições, conclusão)
        """
        return self.regras
    
    def contar_regras(self):
        """
        Retorna o número total de regras
        
        Returns:
            Número inteiro com a quantidade de regras
        """
        return len(self.regras)
    
    def encad_frente(self, fatos):
        """
        Aplica encadeamento para frente (forward chaining)
        Deduz novos fatos a partir de conclusões já obtidas, criando uma cadeia de raciocínio
        
        Args:
            fatos: Lista ou conjunto de fatos observados inicialmente
            
        Returns:
            Dicionário com conclusões, justificativas, fatos usados, fatos iniciais,
            fatos derivados e árvore de dedução
        """
        fatos_conhecidos = set(fatos)  # Conjunto de fatos conhecidos (iniciais + derivados)
        fatos_iniciais = set(fatos)  # Mantém apenas os fatos iniciais
        fatos_derivados = set()  # Fatos derivados durante o processo
        conclusoes = []  # Conclusões finais (diagnósticos)
        justificativas = []  # Justificativas de cada regra ativada
        arvore_deducao = []  # Árvore mostrando como cada fato foi derivado
        regras_ativadas = set()  # Para evitar processar a mesma regra múltiplas vezes
        
        iteracao = 0
        mudou = True  # Flag para verificar se novos fatos foram adicionados
        
        # Algoritmo de forward chaining - itera até ponto fixo
        while mudou and iteracao < self.max_iteracoes:
            mudou = False
            iteracao += 1
            
            # Verifica cada regra
            for idx, (condicoes, conclusao) in enumerate(self.regras):
                # Evita processar regras já ativadas (otimização)
                if idx in regras_ativadas:
                    continue
                
                # Se todas as condições da regra estão presentes nos fatos conhecidos
                if condicoes.issubset(fatos_conhecidos):
                    # Adiciona a conclusão como novo fato (se ainda não estiver presente)
                    # Para forward chaining, tratamos a conclusão como um fato que pode ativar outras regras
                    # Mas também a adicionamos às conclusões finais
                    
                    # Extrai possíveis fatos da conclusão (palavras-chave que podem ser fatos)
                    # Por enquanto, adicionamos a conclusão completa como um "fato derivado"
                    # e também a mantemos como conclusão
                    
                    # Verifica se a conclusão já foi processada
                    if conclusao not in conclusoes:
                        conclusoes.append(conclusao)
                        
                        # Cria justificativa
                        fatos_ativadores = ', '.join(sorted(condicoes))
                        justificativa = f"Regra ativada por: [{fatos_ativadores}] → {conclusao}"
                        justificativas.append(justificativa)
                        
                        # Adiciona à árvore de dedução
                        arvore_deducao.append({
                            'fatos_necessarios': sorted(condicoes),
                            'conclusao': conclusao,
                            'iteracao': iteracao
                        })
                        
                        # Marca que houve mudança
                        mudou = True
                        regras_ativadas.add(idx)
                        
                        # Tenta extrair fatos implícitos da conclusão usando a função da base de conhecimento
                        fatos_extraidos = extrair_fatos_da_conclusao(conclusao)
                        for fato_extraido in fatos_extraidos:
                            if fato_extraido not in fatos_conhecidos:
                                fatos_conhecidos.add(fato_extraido)
                                fatos_derivados.add(fato_extraido)
                                mudou = True
                                
                                # Adiciona à árvore de dedução
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
        """
        Aplica encadeamento híbrido (combinação de backward e forward chaining)
        Primeiro aplica backward chaining, depois usa as conclusões para forward chaining
        
        Args:
            fatos: Lista ou conjunto de fatos observados
            
        Returns:
            Dicionário combinando resultados de ambos os métodos
        """
        # Primeiro passo: backward chaining
        resultado_backward = self.encad_tras(fatos)
        
        # Segundo passo: forward chaining usando fatos iniciais + conclusões do backward
        # Extrai fatos implícitos das conclusões do backward
        fatos_para_forward = set(fatos)
        
        # Adiciona fatos extraídos das conclusões do backward
        for conclusao in resultado_backward['conclusoes']:
            fatos_extraidos = extrair_fatos_da_conclusao(conclusao)
            fatos_para_forward.update(fatos_extraidos)
        
        # Aplica forward chaining
        resultado_forward = self.encad_frente(list(fatos_para_forward))
        
        # Combina resultados
        conclusoes_combinadas = resultado_backward['conclusoes'] + resultado_forward['conclusoes']
        # Remove duplicatas mantendo ordem
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

