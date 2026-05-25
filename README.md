# 🗄️ MySQL Connector Utils

Módulo utilitário em Python para conexão e manipulação de bancos de dados MySQL, feito para ser importado e reutilizado em outros projetos.

---

### 🚀 Funcionalidades

- ✅ Conectar ao servidor MySQL (com ou sem banco selecionado)
- ✅ Criar databases
- ✅ Executar queries de escrita — `INSERT`, `UPDATE`, `DELETE`, `CREATE TABLE`
- ✅ Executar queries de leitura — `SELECT`
- ✅ Queries parametrizadas (proteção contra SQL Injection)
- ✅ Tratamento de erros
- ✅ Fechamento seguro de cursores e conexão

---

### 🛠️ Tecnologias

| Tecnologia | Versão | Uso |
|---|---|---|
| [Python](https://www.python.org/) | 3.13.5 | Linguagem principal |
| [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) | 8.x | Conexão com MySQL |

---

### ⚙️ Como usar

#### 1. Instale a dependência

```bash
pip install mysql-connector-python
```

#### 2. Importe no seu projeto

```python
import manipulador_mysql
```

---

### 📖 Alguns exemplos de uso

**Conectar**

```python
conexao = db.conectar_db(
    nome_host="localhost",
    nome_usuario="root",
    senha_usuario="123456",
    nome_db="escola"
)
```

**Criar tabela**

```python
criar_tabela = """
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT
)
"""

db.executar_query(conexao, criar_tabela)
```

**Inserir dados**

```python
inserir = """
INSERT INTO alunos (nome, idade)
VALUES (%s, %s)
"""

dados = ("João", 22)

db.executar_query(conexao, inserir, dados)
```

**Ler dados**

```python
select = "SELECT * FROM alunos"

resultado = db.ler_query(conexao, select)

for aluno in resultado:
    print(aluno)
```

**Encerrar conexão**

```python
db.fechar_conexao(conexao)
```

---

### 📌 Observações

- As funções `executar_query()` e `ler_query()` aceitam `valores` como tupla para queries parametrizadas — **sempre prefira isso a concatenar strings**, pois evita SQL Injection.
- A função `criar_conexao_servidor()` conecta sem selecionar um banco, útil para criar databases do zero.
- O módulo foi projetado para ser **separado da lógica principal** — importe apenas o que precisar.

---

### 🤝 Contribuindo

Projeto simples e em desenvolvimento, toda contribuição é bem-vinda!

- 💡 Sugestões e ideias
- 🔧 Melhorias no código
- ⭐ Se gostou, deixa uma estrela!
