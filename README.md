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
├── app.py                 # Aplicação Flask principal
├── motorInferencia.py     # Motor de inferência (sistema especialista)
├── baseDeRegras.py        # Base de conhecimento com regras e fatos
├── templates/
│   ├── index.html         # Página principal
│   └── result.html        # Página de resultados
├── static/
│   ├── style.css          # Estilos CSS
│   ├── script.js          # JavaScript principal
│   └── beep_player.js     # Player de beeps
└── README.md
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
