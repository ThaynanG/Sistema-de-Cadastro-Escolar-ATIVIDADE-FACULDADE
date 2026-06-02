from conexao import conectar_banco

def listar_alunos():
    conn = conectar_banco()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, nome, data_nascimento, cpf, email 
        FROM alunos 
        ORDER BY nome
    """)
    
    alunos = cursor.fetchall()
    
    print("\n" + "="*90)
    print("                     LISTA DE ALUNOS")
    print("="*90)
    print(f"{'ID':<5} {'NOME':<35} {'DATA NASC':<12} {'CPF':<15} {'EMAIL':<20}")
    print("-"*90)
    
    if not alunos:
        print("❌ Nenhum aluno cadastrado!")
    else:
        for aluno in alunos:
            nome = aluno[1][:33] + "..." if len(aluno[1]) > 35 else aluno[1]
            print(f"{aluno[0]:<5} {nome:<35} {aluno[2] or '---':<12} {aluno[3]:<15} {aluno[4] or '---':<20}")
    
    print("="*90)
    cursor.close()
    conn.close()
