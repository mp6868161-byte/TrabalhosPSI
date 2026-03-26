Este projeto foi desenvolvido com fins pedagógicos por um aluno do Curso Profissional de Gestão e Programação de Sistemas Informáticos (GPSI) – 10.º ano.

O objetivo principal é demonstrar como implementar operações CRUD (Create, Read, Update, Delete) em Python utilizando:

funções (sem classes)
dicionários
separação por ficheiros
validação de dados
menus em terminal
O projeto simula a gestão da entidade Utilizador.

🎯 Objetivos Pedagógicos
Com este projeto os alunos devem aprender a:

organizar código em múltiplos ficheiros Python
utilizar dicionários como estrutura de armazenamento
implementar operações CRUD
validar dados introduzidos pelo utilizador
gerar identificadores automáticos
trabalhar com datas em Python
separar lógica de negócio da interface (menu)
📂 Estrutura do Projeto
.
└──gestor de concertos
     ├── main.py
     ├── Bilhetes.py
     ├── utils.py
└── README.md
main.py
Contém o menu interativo em terminal.

Responsável apenas por:

apresentar opções
recolher dados do utilizador
chamar funções do módulo utilizador
Não contém validações.

utilizador.py
Contém todas as operações CRUD da entidade Utilizador:

criar utilizador
listar utilizadores
consultar utilizador
atualizar utilizador
remover utilizador
Também inclui validações como:

verificação de datas
geração automática de ID
Os utilizadores são guardados num dicionário em memória.

utils.py
Contém funções auxiliares:

geração automática de IDs
validação de datas no formato:
YYYY-MM-DD
👤 Estrutura da Entidade Utilizador
Cada utilizador contém:

id_utilizador
nome
email
tipo_conta (free / premium)
data_nascimento
Exemplo:

U001
Nome: Ana Silva
Email: ana@email.pt
Tipo: premium
Data nascimento: 2007-03-12
▶️ Como Executar o Projeto
1️⃣ Garantir que Python está instalado

2️⃣ Executar no terminal:

python main.py
3️⃣ Utilizar o menu apresentado

📚 Conceitos Trabalhados
Este projeto permite consolidar:

funções
dicionários
módulos Python
importação entre ficheiros
validação de dados
estruturas condicionais
ciclos (while)
👨‍🏫 Utilização em Sala de Aula
Este projeto vai ser usado para:

introdução ao CRUD
exercícios guiados
avaliação prática
preparação para projetos maiores

