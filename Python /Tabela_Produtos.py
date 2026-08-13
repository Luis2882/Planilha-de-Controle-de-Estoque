
# Importa o SQLite3
import sqlite3 

# 1. Conecta ao banco de dados
conexao = sqlite3.connect("estoque.db")

# 2. Cria o cursor 
cursor = conexao.cursor()

# 3. Cria uma tabela
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL UNIQUE,
    quantidade_produto INTEGER,
    valor_produto REAL 
    )
"""
)

lista_produtos = [
    ("Mouse Gamer", 53, 120.50),
    ("Monitor Gamer", 39, 520.50),
    ("Teclado Gamer", 46, 150.00),
    ("Mousepad Gamer", 52, 70.00),
    ("Cadeira Gamer", 34, 750.00),
    ("Headset Gamer",45, 250.00),
    ("Mesa",36, 430.00),
    ("Soundbar",56, 85.00),
    ("Suporte Articulado Monitor",49, 110.00),
    ("Controle Gamer",61, 320.00),
    ("Microfone",56, 270.00),
    ("Braço Articulado Microfone",38, 120.00),
]

cursor.executemany(
    """
INSERT OR IGNORE INTO produtos (nome_produto, quantidade_produto, valor_produto)
VALUES (?,?,?)
""",
    lista_produtos,
)

# 4. Salva as alterações
conexao.commit()

# Fecha a conexão
conexao.close()

print(" Tabela 'produtos' criada com sucesso! E produto inserido. ")


