 🛒 Sistema de Gestão de Produtos (Python + Tkinter + PostgreSQL)



Este projeto é uma aplicação desktop desenvolvida em Python com interface gráfica utilizando Tkinter, integrada a um banco de dados PostgreSQL.

O sistema permite realizar operações completas de CRUD (Create, Read, Update, Delete) para o gerenciamento de produtos.

---

## 🚀 Funcionalidades

* ✅ Cadastro de produtos
* 📋 Listagem de produtos
* ✏️ Atualização de dados
* ❌ Exclusão de produtos
* 🧹 Limpeza de campos
* 🖥️ Interface gráfica interativa com tabela (Treeview)

---

## 🛠️ Tecnologias utilizadas

* Python
* Tkinter
* PostgreSQL
* Psycopg2
* Faker (para geração de dados de teste)

---

## 📂 Estrutura do projeto

```
📁 projeto
 ├── appGui.py        # Interface gráfica
 ├── appBD.py         # Regras de negócio e CRUD
 ├── conexao.py       # Conexão com banco de dados
 └── README.md        # Documentação
```

---

## ⚙️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install psycopg2 faker
```

### 2. Configurar o banco de dados

No arquivo `conexao.py`, altere conforme seu ambiente:

```python
host="localhost"
database="produtos1"
user="postgres"
password="1234"
port="5432"
```

### 3. Executar o projeto

```bash
python appGui.py
```

---

## 🗄️ Banco de dados

A tabela é criada automaticamente:

```sql
CREATE TABLE PRODUTO (
    Codigo SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Preco DECIMAL(10,2) NOT NULL
);
```

---

## 📸 Demonstração

> (Adicione aqui prints da aplicação rodando)

Sugestão:

* Tela principal
* Cadastro de produto
* Tabela preenchida

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar:

* Integração entre Python e banco de dados
* Desenvolvimento de interfaces gráficas
* Operações CRUD
* Organização de código em camadas

---

## 📈 Melhorias futuras

* 🔍 Busca de produtos
* 📊 Ordenação e filtros
* 🎨 Melhorias visuais (UI/UX)
* 📦 Empacotamento como executável (.exe)

---

## 👨‍💻 Autor

Desenvolvido por Junior

---


