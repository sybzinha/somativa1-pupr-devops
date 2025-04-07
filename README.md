# 🛒 FastAPI Shopping List API

Esta é uma API desenvolvida com **FastAPI** para gerenciar um catálogo simples de produtos.  
Ela permite realizar operações básicas de **CRUD** (Create, Read, Update, Delete) e já conta com alguns produtos pré-cadastrados para testes.  
Ideal para fins educacionais e projetos de estudo. 👨‍💻📚

---

## 📌 Funcionalidades

A API oferece os seguintes endpoints:

| Método   | Rota                          | Descrição                                                                 |
|----------|-------------------------------|---------------------------------------------------------------------------|
| `GET`    | `/products`                   | 📋 Lista todos os produtos cadastrados                                    |
| `GET`    | `/products/{id}`              | 🔎 Retorna os detalhes de um produto específico pelo seu ID               |
| `GET`    | `/products/search?name=nome`  | 🕵️‍♀️ Filtra produtos pelo nome informado via query param (`name`)       |
| `POST`   | `/products`                   | ➕ Cadastra um novo produto na lista                                       |
| `PUT`    | `/products/{id}`              | ♻️ Atualiza completamente os dados de um produto existente                |
| `DELETE` | `/products/{id}`              | ❌ Remove um produto do sistema com base no ID                            |

---

## 🧾 Exemplos de Produtos Cadastrados

- 🧃 Monster Energy  
- 🧁 Yakult 
- 🍕 Pizza Pepperoni  
- 🐔 Nuggets  
- 🌮 Doritos 
- 🥤 Coca-Cola
- 💜 Açaí
- 🍫 Chocolate 

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório:
```bash
git clone git@github.com:sybzinha/somativa1-devops-pucpr.git
cd somativa1-devops-pucpr
```

### 2. Instale as dependências:
```bash
pip install "fastapi[standard]"
```

### 3. Execute o servidor:
```bash
fastapi dev main.py 
```