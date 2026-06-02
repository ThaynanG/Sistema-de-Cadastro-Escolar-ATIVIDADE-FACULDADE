from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from conexao import conectar_banco
import os

app = Flask(__name__)
CORS(app)

# ==================== ENDPOINTS DA API ====================

@app.route('/api/alunos', methods=['GET'])
def listar_alunos():
    """Lista todos os alunos"""
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, data_nascimento, cpf, email FROM alunos ORDER BY id DESC")
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(alunos)

@app.route('/api/alunos', methods=['POST'])
def cadastrar_aluno():
    """Cadastra um novo aluno"""
    dados = request.json
    
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO alunos (nome, data_nascimento, cpf, email)
            VALUES (%s, %s, %s, %s)
        ''', (dados['nome'], dados['data_nascimento'], dados['cpf'], dados.get('email', '')))
        
        conn.commit()
        novo_id = cursor.lastrowid
        cursor.close()
        conn.close()
        
        return jsonify({'mensagem': 'Aluno cadastrado com sucesso!', 'id': novo_id}), 201
        
    except Exception as e:
        conn.close()
        return jsonify({'erro': str(e)}), 400

@app.route('/api/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    """Atualiza um aluno"""
    dados = request.json
    
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE alunos 
        SET nome = %s, data_nascimento = %s, cpf = %s, email = %s
        WHERE id = %s
    ''', (dados['nome'], dados['data_nascimento'], dados['cpf'], dados.get('email', ''), id))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'mensagem': 'Aluno atualizado com sucesso!'})

@app.route('/api/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    """Deleta um aluno"""
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'mensagem': 'Aluno excluído com sucesso!'})

@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    """Retorna estatísticas"""
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM alunos")
    total_alunos = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    
    return jsonify({'total_alunos': total_alunos})

@app.route('/api/buscar', methods=['GET'])
def buscar_alunos():
    """Busca alunos por nome ou CPF"""
    termo = request.args.get('q', '')
    
    conn = conectar_banco()
    if not conn:
        return jsonify({'erro': 'Erro na conexão'}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute('''
        SELECT id, nome, data_nascimento, cpf, email 
        FROM alunos 
        WHERE nome LIKE %s OR cpf LIKE %s
        ORDER BY nome
    ''', (f'%{termo}%', f'%{termo}%'))
    
    alunos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(alunos)

if __name__ == '__main__':
    print("="*50)
    print("🚀 API SISTEMA ESCOLA - WEB")
    print("="*50)
    print(f"📍 API: http://localhost:5000")
    print(f"📊 Dashboard: http://localhost:5000/api/dashboard")
    print(f"📋 Alunos: http://localhost:5000/api/alunos")
    print("="*50)
    app.run(debug=True, port=5000)
