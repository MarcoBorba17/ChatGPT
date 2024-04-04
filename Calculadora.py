import tkinter as tk
import sqlite3

# Conectar ao banco de dados SQLite3
conn = sqlite3.connect('calculadora.db')
cursor = conn.cursor()

# Criar tabela para armazenar as operações, se ela não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS operacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operacao TEXT NOT NULL,
    resultado TEXT NOT NULL
)
''')
conn.commit()

# Função para executar e salvar a operação
def executar_operacao(operacao):
    try:
        # Calcular o resultado
        resultado = str(eval(operacao))
        # Salvar a operação e o resultado no banco de dados
        cursor.execute('INSERT INTO operacoes (operacao, resultado) VALUES (?, ?)', (operacao, resultado))
        conn.commit()
        return resultado
    except Exception as e:
        return str(e)

# Função para atualizar a entrada com o resultado
def calcular():
    resultado = executar_operacao(entrada.get())
    entrada.delete(0, tk.END)
    entrada.insert(0, resultado)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Criar a entrada para exibir a operação e o resultado
entrada = tk.Entry(root, width=40, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Definir os botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Criar e posicionar os botões
for (texto, linha, coluna) in botoes:
    botao = tk.Button(root, text=texto, width=10, height=3, command=lambda t=texto: entrada.insert(tk.END, t))
    botao.grid(row=linha, column=coluna)
    if texto == '=':
        botao.config(command=calcular)

# Executar a aplicação
root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()
