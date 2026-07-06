# 🏋️‍♂️ Sistema de Academia — Terminal CRUD

Este é um sistema de terminal para gerenciamento de alunos de uma academia, desenvolvido em **Python** e integrado com um banco de dados **MySQL**. O projeto foi construído como parte de um trabalho acadêmico para praticar conceitos de CRUD, prevenção de SQL Injection, Programação Orientada a Objetos (POO) e manipulação de banco de dados.

---

## 🚀 Funcionalidades

O sistema conta com um menu interativo com as seguintes opções:
1. **Cadastrar Aluno:** Insere um novo aluno associando-o a um plano existente.
2. **Buscar Aluno:** Busca flexível por nome (parcial).
3. **Listar Todos:** Exibe todos os alunos cadastrados utilizando o mapeamento da classe `Aluno`.
4. **Atualizar Aluno (Bônus):** Permite alterar todos os dados de um aluno através do seu ID.
5. **Remover Aluno (Bônus):** Exclui o registro de um aluno permanentemente do banco através do seu ID.
0. **Sair:** Encerra a conexão com o banco com segurança e fecha o programa.

---

## 🛠️ Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* **Python 3.x**
* **MySQL Server**
* Um editor de código (como o **VS Code**)

---

## 📦 Como Rodar o Projeto Localmente

Siga o passo a passo abaixo para configurar e executar o projeto na sua máquina:

### 1. Clonar o Repositório
Abra o seu terminal e clone este repositório;

### 2. Instalar Dependências
Antes de iniciar a instalação dos pacotes, crie um ambiente .venv em sua máquina, para que possa instalar os pacotes de maneira segura, garantindo que só funiconem nesse ambiente.
Este projeto utiliza bibliotecas externas para conectar ao MySQL e ler variáveis de ambiente. Instale-as com o comando: 
```bash
pip install mysql-connector-python python-dotenv
```

### 3. Configurar o Banco de Dados (MySQL)
Para facilitar os seus testes, deixei o script SQL de criação das tabelas e população inicial na raiz do projeto.
  1. Abra o seu gerenciador de banco de dados (MySQL Workbench, DBeaver, etc.).
  2. Execute o script contido no arquivo Academia_Dev.sql para criar o banco de dados, as tabelas de alunos e planos, e inserir os dados iniciais.

### 4. Configurar as Variáveis de Ambiente (.env)
Por motivos de segurança, as credenciais do banco de dados não são enviadas para o GitHub (estão protegidas pelo .gitignore). Você precisará criar esse arquivo localmente.
  1. Na raiz do projeto, crie um arquivo chamado exatamente .env
  2. Adicione as seguintes variáveis e substitua pelos dados do seu MySQL local:

     DB_HOST=localhost
     
     DB_USER=seu_usuario_do_mysql
     
     DB_PASSWORD=sua_senha_do_mysql
     
     DB_NAME=nome_do_seu_banco_de_dados

### 5. Executar o Programa
Agora é só rodar o script principal do Python:
```bash
python sistema.py
```

---

## 🔒 Segurança Aplicada (SQL Injection)
Todas as consultas feitas ao banco de dados que envolvem entradas do usuário utilizam marcadores de posição (%s) em vez de formatação direta de strings (f-strings). Isso garante que dados maliciosos sejam interpretados estritamente como texto, blindando a aplicação contra ataques de injeção de SQL.

---

## 🛠️ Tecnologias Utilizadas
- Python
- MySQL
- mysql-connector-python (Driver oficial do MySQL para Python)
- python-dotenv (Gerenciamento de credenciais seguras)
