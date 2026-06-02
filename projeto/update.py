from conexao import conectar_banco

def atualizar_aluno():
    conn = conectar_banco()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("        ATUALIZAR ALUNO")
    print("="*50)
    
    id_aluno = input("Digite o ID do aluno: ")
    
    # Buscar dados atuais
    cursor.execute("SELECT id, nome, email FROM alunos WHERE id = %s", (id_aluno,))
    aluno = cursor.fetchone()
    
    if not aluno:
        print("❌ Aluno não encontrado!")
        cursor.close()
        conn.close()
        return
    
    print(f"\n📌 Aluno: {aluno[1]}")
    print(f"📧 Email: {aluno[2]}")
    print("-"*30)
    
    novo_nome = input(f"Novo nome (Enter para manter): ").strip()
    novo_email = input(f"Novo email (Enter para manter): ").strip()
    
    nome_final = novo_nome if novo_nome else aluno[1]
    email_final = novo_email if novo_email else aluno[2]
    
    sql = "UPDATE alunos SET nome = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (nome_final, email_final, id_aluno))
    conn.commit()
    
    print(f"\n✅ Aluno atualizado com sucesso!")
    
    cursor.close()
    conn.close()
