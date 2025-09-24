from aluno import Aluno
from crud import create_aluno, read_aluno_by_id, read_alunos, update_aluno, delete_aluno
from banco import init_db

def main():
    # Inicializa o banco de dados e garante que a tabela existe
    init_db()

    print("=== TESTANDO CRUD ===")

    # Criando um aluno de exemplo
    aluno1 = Aluno("João Silva", "12345678900", "2000-05-10", "ativo")

    # CREATE
    novo_id = create_aluno(aluno1)
    print(f"Novo aluno criado com ID: {novo_id}")

    # READ por ID
    print("\nBuscando aluno criado...")
    print(read_aluno_by_id(novo_id))

    # READ lista
    print("\nListando todos os alunos:")
    print(read_alunos())

    # UPDATE
    print("\nAtualizando status do aluno...")
    update_aluno(novo_id, {"status": "inativo"})
    print(read_aluno_by_id(novo_id))

    # DELETE
    print("\nRemovendo aluno...")
    delete_aluno(novo_id)
    print(read_aluno_by_id(novo_id))  # Deve retornar None


if __name__ == "__main__":
    main()
