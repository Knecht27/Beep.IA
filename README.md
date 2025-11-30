# Beep.IA

Sistema especialista em suporte técnico na área de TI feito em Python. O Beep.IA é uma aplicação web que utiliza técnicas de inteligência artificial (sistemas especialistas) para diagnosticar problemas de hardware de computadores baseado em códigos de beeps da BIOS e outros sintomas.

## Funcionalidades

- **Diagnóstico de Beeps da BIOS**: Suporta múltiplos fabricantes (AMI, Award, Phoenix, Dell, ASUS, GIGABYTE, MSI, HP/Compaq, IBM)
- **Múltiplos Métodos de Inferência**:
  - Encadeamento para trás (Backward Chaining)
  - Encadeamento para frente (Forward Chaining)
  - Encadeamento híbrido (combinação de ambos)
- **Diagnóstico de Outros Problemas**: Detecta problemas como superaquecimento, tela azul, travamentos, etc.
- **Interface Web Amigável**: Interface moderna e responsiva com Bootstrap
- **Reprodução de Beeps**: Permite ouvir os padrões de beeps para facilitar a identificação

## Estrutura do Projeto

```
Beep.IA/
├── app.py                      # Aplicação Flask principal
├── requirements.txt           # Dependências do projeto
├── Procfile                   # Configuração para deploy (Heroku)
├── .runtime.txt              # Versão do Python
├── README.md                 # Documentação principal
│
├── core/                      # Módulo principal do sistema
│   ├── domain/               # Conhecimento do domínio
│   │   ├── dados.py         # Fabricantes, beeps e outros erros
│   │   ├── regras.py        # Regras de diagnóstico
│   │   └── mapeamento.py    # Mapeamento para forward chaining
│   │
│   ├── inference/            # Motor de inferência
│   │   └── motor_inferencia.py  # Backward, Forward e Híbrido
│   │
│   └── utils/                # Utilitários
│       └── justificativa.py    # Formatação de justificativas
│
├── templates/                # Templates HTML (Jinja2)
│   ├── index.html
│   └── result.html
│
└── static/                   # Arquivos estáticos
    ├── style.css
    ├── script.js
    └── beep_player.js
```

## Requisitos

- Python 3.7 ou superior
- Flask
- Navegador web moderno
- Gunicorn


## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd Beep.IA
```

2. Instale as dependências:
```bash
pip install flask
```

## Como Executar

1. Execute a aplicação:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```


## Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **IA**: Sistemas Especialistas (Rule-Based Systems)
- **Métodos de Inferência**: Backward Chaining, Forward Chaining


## Licença

Este projeto é de código aberto e está disponível para uso educacional e comercial.
