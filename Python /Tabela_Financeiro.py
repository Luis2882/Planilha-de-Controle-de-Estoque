
import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

cursor.execute(
"""
    CREATE TABLE IF NOT EXISTS financeiro_produtos(
    id_produto INTEGER PRIMARY KEY,
    custo_fabricacao REAL,
    lucro_estimado REAL,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
    )
"""
)

# Lista com dados do financeiro ( id_produto, custo_fabricacao, lucro_estimado)
lista_financeiro = [
    (1, 50.00, 70.50),
    (2, 70.00, 80.00),
    (3, 100.00, 100.00),
    (4, 400.00, 350.50),
    (5, 30.00, 40.00),
    (6, 300.00, 220.50),
    (7, 200.00, 230.00),
    (8, 40.00, 45.00),
    (9, 50.00, 60.00),
    (10, 150.00, 170.00),
    (11, 120.00, 150.00),
    (12, 50.00, 70.00),

]
cursor.executemany(
"""

INSERT OR IGNORE INTO financeiro_produtos (id_produto, custo_fabricacao, lucro_estimado) 
VALUES (?,?,?)

""",
lista_financeiro

)

conexao.commit()
conexao.close()

print("Dados Finaceiros Inseridos!")


