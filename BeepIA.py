BaseDeConhecimento = {
    "1 Bip Curto": "O sistema iniciou normalmente.",
    "2 Bips Curtos": "Erro de definição da CMOS (Bios).",
    "1 Bip Longo e 1 Curto": "Erro de Memória ou Placa-mãe. Verifique os módulos de RAM e sua conexão.",
    "1 Bip Longo e 2 Curtos": "Erro de Placa de vídeo ou Monitor. Verifique a placa de vídeo e os cabos do monitor.",
    "1 Bip Longo e 3 Curtos": "Erro de Teclado. Verifique se o teclado está bem conectado.",
    "1 Bip Longo e 9 Curtos": "Erro da Rom Bios (problema físico da Bios mesmo).",
    "Longos Bips Contínuos": "Problema com a memória Ram. Tente limpar os contatos ou testar os módulos um a um.",
    "Curtos Bips Contínuos": "Problema de Energia (fonte normalmente). Verifique a fonte de alimentação e seus cabos."
}

def DiagnosticarProblema(sintoma):
    if sintoma in BaseDeConhecimento:
        return BaseDeConhecimento[sintoma]
    else:
        return "Sintoma não encontrado na base de conhecimento."

def Interface():
    print("--- Sistema Especialista de Diagnóstico de Bipes da BIOS ---")
    print("Por favor, selecione o sintoma que seu computador está apresentando:")

    ListaDeSintomas = list(BaseDeConhecimento.keys())
    for i, sintoma in enumerate(ListaDeSintomas):
        print(f"{i + 1}. {sintoma}")

    try:
        escolha = int(input("\nDigite o número correspondente ao sintoma: "))
        if 1 <= escolha <= len(ListaDeSintomas):
            SintomaSelecionado = ListaDeSintomas[escolha - 1]
            
            diagnostico = DiagnosticarProblema(SintomaSelecionado)
            
            print("\n--- Diagnóstico ---")
            print(f"Sintoma informado: {SintomaSelecionado}")
            print(f"Conclusão: {diagnostico}")
            print("-------------------\n")
        else:
            print("Opção inválida. Por favor, reinicie e escolha um número da lista.")
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas o número.")

if __name__ == "__main__":
    Interface()