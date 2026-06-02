from insert import cadastrar_aluno
from listar_alunos import listar_alunos
from update import atualizar_aluno
from delete import deletar_aluno
from conexao import conectar_banco
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        limpar_tela()
        print("="*50)
        print("        SISTEMA ESCOLA")
        print("="*50)
        print("   1 - Cadastrar aluno")
        print("   2 - Listar alunos")
        print("   3 - Atualizar aluno")
        print("   4 - Excluir aluno")
        print("   5 - Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_aluno()
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            listar_alunos()
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            atualizar_aluno()
            input("\nPressione Enter para continuar...")
        elif opcao == "4":
            deletar_aluno()
            input("\nPressione Enter para continuar...")
        elif opcao == "5":
            print("\n👋 Encerrando sistema...")
            break
        else:
            print("\n❌ Opção inválida!")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    menu()
