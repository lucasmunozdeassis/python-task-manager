# Gerenciador de Tarefas

Aplicação web minimalista para gerenciamento de tarefas desenvolvida em Python com Flask, utilizando armazenamento em JSON e templates Jinja2.

## Funcionalidades

- **Criar**: Adiciona tarefas com título e status (Pendente ou Feito).
- **Listar**: Exibe a lista de tarefas atualizada na página inicial.
- **Deletar**: Remove tarefas individualmente.
- **Persistência**: Dados salvos em arquivo JSON local (`tarefas.json`).

## Tecnologias

- Python
- Flask
- HTML5 / CSS3

## Como Executar

1. Clone o repositório e acesse a pasta:
   ```bash
   git clone [https://github.com/lucasmunozdeassis/python-task-manager.git]
   
   cd seu-repositorio

    Crie e ative o ambiente virtual:
    Bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
# No Windows: venv\Scripts\activate

Instale o Flask:
Bash

pip install flask

Inicie a aplicação:
Bash

    python app.py

    Acesse no navegador: http://127.0.0.1:5000

Desenvolvido por Lucas Fernando Muñoz de Assis.