from conexao import conectar_banco

def deletar_aluno():
    conn = conectar_banco()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("        EXCLUIR ALUNO")
    print("="*50)
    
    id_aluno = input("Digite o ID do aluno: ")
    
    # Buscar dados atuais
    cursor.execute("SELECT nome FROM alunos WHERE id = %s", (id_aluno,))
    aluno = cursor.fetchone()
    
    if not aluno:
        print("❌ Aluno não encontrado!")
        cursor.close()
        conn.close()
        return
    
    print(f"\n⚠️ ALUNO: {aluno[0]}")
    confirmar = input("Tem certeza que deseja excluir? (s/N): ").lower()
    
    if confirmar == 's':
        sql = "DELETE FROM alunos WHERE id = %s"
        cursor.execute(sql, (id_aluno,))
        conn.commit()
        print(f"\n✅ Aluno '{aluno[0]}' excluído com sucesso!")
    else:
        print("\n❌ Operação cancelada!")
    
    cursor.close()
    conn.close()
