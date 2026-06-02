from conexao import conectar_banco

def cadastrar_aluno():
    conn = conectar_banco()
    if not conn:
        return
    
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("        CADASTRO DE ALUNO")
    print("="*50)
    
    nome = input("Nome completo: ").strip()
    data = input("Data nascimento (AAAA-MM-DD): ").strip()
    cpf = input("CPF (apenas números): ").strip()
    email = input("Email: ").strip()
    
    try:
        sql = """
            INSERT INTO alunos (nome, data_nascimento, cpf, email)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (nome, data, cpf, email))
        conn.commit()
        print(f"\n✅ Aluno '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao cadastrar: {e}")
    finally:
        cursor.close()
        conn.close()
