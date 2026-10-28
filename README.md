Task Manager (Gerenciador de Tarefas)

Uma aplicação web minimalista e funcional para gerenciamento de tarefas do dia a dia, desenvolvida em Python utilizando o microframework Flask, armazenamento leve em arquivo JSON e renderização dinâmica com Jinja2.

Funcionalidades

Criar Tarefas: Adicione novas tarefas informando o nome e o status inicial (Pendente ou Feito).

Listar Tarefas: Visualize todas as suas tarefas cadastradas na página principal em tempo real.

Marcar como Concluída: Altere o status de qualquer tarefa para "concluído" com um único clique.

Reverter Status: Altere tarefas concluídas de volta para "Pendente".

Excluir Tarefas: Remova tarefas que não são mais necessárias.

Persistência de Dados: Salvamento automático em um arquivo local (tarefas.json), garantindo que seus dados não sejam perdidos ao fechar a aplicação.


Tecnologias Utilizadas

Backend: Python 3, Flask

Frontend: HTML5, CSS3, Jinja2 (Template Engine)

Armazenamento: JSON (persistência local)



Estrutura do Projeto

python-task-manager/
│
├── static/
│   └── style.css          # Estilização da aplicação
├── templates/
│   ├── index.html         # Página principal (Listagem de tarefas)
│   └── form.html          # Formulário de criação de tarefas
├── app.py                 # Rotas e lógica da aplicação Flask
├── tarefas.json           # Arquivo de persistência dos dados
└── README.md              # Documentação do projeto


Como Executar o Projeto

Pró-requisitos

Certifique-se de ter o Python instalado em sua máquina.

Passo a Passo

Clonar o repositório:

git clone https://github.com/lucasmunozdeassis/python-task-manager.git
cd python-task-manager


Criar e ativar um ambiente virtual:

Linux / macOS:

python3 -m venv venv
source venv/bin/activate


Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


Windows (Prompt de Comando - CMD):

python -m venv venv
venv\Scripts\activate.bat


Instalar as dependências:

pip install flask


Executar a aplicação:

python app.py


Acessar no navegador:
Acesse a URL: http://127.0.0.1:5000


Autor

Desenvolvido por Lucas Fernando Muñoz de Assis.

Sinta-se à vontade para contribuir com melhorias, novos recursos ou correções de bugs!