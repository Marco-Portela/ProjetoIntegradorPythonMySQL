# Importando os módulos que serão utilizados nesse projeto
import os # módulo que permite a interação com o sistema operacional
import mysql.connector # módulo que realiza a conexão com o banco de dados
from dotenv import load_dotenv # módulo dotenv para deixar dados sensíveis ocultos dentro de um arquivo .env, sendo que essas variáveis serão carregadas como variáveis de ambiente

load_dotenv() # carregar as ariáveis ambiente do .env

# Definindo a classe para representar o aluno, utilizando por base os dados da tabela_alunos, do banco de dados
class Aluno:
    def __init__(self, id, nome, data_matricula, ativo, plano_id):
        self.id = id
        self.nome = nome
        self.data_matricula = data_matricula
        self.ativo = ativo
        self.plano_id = plano_id

    def __str__(self):
        situacao = "ativo" if self.ativo else "inativo"
        return f"[{self.id}] {self.nome} — matrícula: {self.data_matricula} | {situacao}"

# Definindo a função que realiza o cadastro de um novo aluno e salva em nosso banco de dados
def cadastrar(conexao, cursor):
    # Apresenta os campos que devém ser preenchidos pelo usuário
    print("\n--- Cadastrar novo aluno ---")
    nome = input("Nome do aluno: ")
    data_matricula = input("Data de matrícula (AAAA-MM-DD): ")
    ativo = input("Está ativo? (1 = sim, 0 = não): ")

    # Mostra os planos disponíveis para o usuário escolher
    print("\nPlanos disponíveis:")
    cursor.execute("SELECT id, nome, valor_mensalidade FROM tabela_planos")
    for plano in cursor.fetchall():
        print(plano)
    plano_id = input("Digite o id do plano: ")

    # INSERT seguro: %s (marcador de posição) no comando, valores separados na tupla
    cursor.execute(
        "INSERT INTO tabela_alunos (nome, data_matricula, ativo, plano_id) VALUES (%s, %s, %s, %s)",
        (nome, data_matricula, ativo, plano_id)
    )
    conexao.commit()
    print("Aluno cadastrado com sucesso!")

# Definindo a função que realiza a consulta de um aluno, ataravés do nome preterido pelo usuário
def buscar(cursor):
    print("\n--- Buscar Aluno ---")
    nome = input("Digite o nome do aluno: ")
    
    # Usamos LIKE e colocamos % ao redor do nome para buscar por partes do nome
    # O %s protege contra SQL Injection
    buscar_sql = "SELECT id, nome, data_matricula, ativo, plano_id FROM tabela_alunos WHERE nome LIKE %s"
    
    # Executa passando a variável protegida na tupla
    cursor.execute(buscar_sql, (f"%{nome}%",))
    
    # Pega todos os resultados que o banco encontrou
    resultados_buscar = cursor.fetchall()
    
    if not resultados_buscar:
        print("Nenhum aluno encontrado com esse nome. Tente novamente!")
        return

    print("\nResultados encontrados:")
    for linha in resultados_buscar:
        # A 'linha' é uma tupla. O asterisco (*) desempacota a tupla.
        # É o mesmo que fazer: Aluno(linha[0], linha[1], linha[2], linha[3], linha[4])
        aluno = Aluno(*linha)
        print(aluno)

# Definindo a função que exibe os dados de todos os alunos cadastrados em nossa base dados
def listar(cursor):
    print("\n--- Lista de Todos os Alunos ---")
    
    # Seleciona todos os alunos do banco
    listar_sql = "SELECT id, nome, data_matricula, ativo, plano_id FROM tabela_alunos"
    cursor.execute(listar_sql)
    
    # Pega todos os resultados
    resultados_listar = cursor.fetchall()
    
    if not resultados_listar:
        print("Nenhum aluno cadastrado no sistema ainda.")
        return

    for linha in resultados_listar:
        # Instancia o objeto Aluno e o print aciona automaticamente o __str__
        aluno = Aluno(*linha)
        print(aluno)

# Definindo a função que atualiza os dados de um determinado id de aluno em nossa base de dados, para os dados que o usuário preencher
def atualizar(conexao, cursor):
    print("\n--- Atualizar Aluno ---")
    id_aluno = input("Digite o ID do aluno que deseja atualizar: ")
    
    # Pedimos os novos dados
    nome = input("Novo nome do aluno: ")
    data_matricula = input("Nova data de matrícula (AAAA-MM-DD): ")
    ativo = input("Está ativo? (1 = sim, 0 = não): ")
    plano_id = input("Novo ID do plano: ")

    # Comando UPDATE do SQL
    comando_sql = "UPDATE tabela_alunos SET nome = %s, data_matricula = %s, ativo = %s, plano_id = %s WHERE id = %s"
    
    # A tupla agora tem os 4 campos novos + o ID que vai no WHERE
    cursor.execute(comando_sql, (nome, data_matricula, ativo, plano_id, id_aluno))
    
    # Como alteramos o banco de dados, precisamos "salvar" (commit)
    conexao.commit()

    # O rowcount nos diz quantas linhas foram modificadas no banco
    if cursor.rowcount > 0:
        print("Cadastro do aluno atualizado com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID (ou os dados digitados já eram iguais aos anteriores).")

# Definindo a função que remove os dados de um determinado id de aluno de nossa base de dados, de acordo com a informação passada pelo usuário
def remover(conexao, cursor):
    print("\n--- Remover Aluno ---")
    id_aluno = input("Digite o ID do aluno que deseja EXCLUIR: ")

    # Comando DELETE do SQL
    comando_sql = "DELETE FROM tabela_alunos WHERE id = %s"
    
    # Passamos o ID em uma tupla de um único item
    cursor.execute(comando_sql, (id_aluno,))
    
    # Confirmamos a exclusão no banco
    conexao.commit()

    # O rowcount nos diz quantas linhas foram modificadas no banco
    if cursor.rowcount > 0:
        print("Aluno removido do sistema com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")

def menu():
    conexao = None
    cursor = None
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conexao.cursor()

        while True:
            print("\n=== Sistema da Academia ===")
            print("1. Cadastrar")
            print("2. Buscar")
            print("3. Listar todos")
            print("4. Atualizar aluno")
            print("5. Remover aluno")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar(conexao, cursor)
            elif opcao == "2":
                buscar(cursor)
            elif opcao == "3":
                listar(cursor)
            elif opcao == "4":
                atualizar(conexao, cursor)
            elif opcao == "5":
                remover(conexao, cursor)
            elif opcao == "0":
                print("Encerrando...\n.\n.\n.")
                print('Sessão encerrada com sucesso!')
                break
            else:
                print("Opção inválida. Tente novamente.")

    except mysql.connector.Error as erro:
        print("Erro ao acessar o banco de dados:", erro)
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()

menu()
