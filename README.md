
# Sistema Financeiro Familiar - Python com SQLAlchemy

Este repositório contém um exemplo de sistema de gerenciamento financeiro familiar, utilizando Python com SQLAlchemy para manipulação de um banco de dados MySQL.

## 📋 Descrição do Projeto

O projeto define quatro tabelas principais no banco de dados:
1. **Categoria**: Armazena informações sobre as categorias de despesas e receitas.
2. **Conta**: Armazena informações sobre diferentes contas financeiras.
3. **Usuários**: Armazena informações dos usuários do sistema.
4. **Finanças**: Registra as transações financeiras associando categorias, contas e usuários.

Cada tabela é representada por uma classe Python usando SQLAlchemy e permite operações básicas como adicionar, listar, atualizar e remover registros.

## 🚀 Tecnologias Utilizadas

- Python
- SQLAlchemy
- MySQL

## 📦 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/alesauer/SQL-Manipular-Dados-Consultas-Python.git
    ```

2. **Instale as dependências**:
    ```bash
    pip install sqlalchemy pymysql
    ```

3. **Configure a conexão com o banco de dados**:
    No arquivo `sistema_financeiro_familiar_completo.py`, ajuste a variável `DATABASE_URL` com as credenciais do seu banco de dados MySQL.

4. **Execute o script**:
    ```bash
    python sistema_financeiro_familiar_completo.py
    ```

## 📚 Funções Disponíveis

### Categoria
- `adicionar_categoria(desc_categoria, obs_categoria=None)`: Adiciona uma nova categoria.
- `listar_categorias()`: Lista todas as categorias.
- `atualizar_categoria(idcategoria, nova_descricao, nova_obs=None)`: Atualiza uma categoria existente.
- `remover_categoria(idcategoria)`: Remove uma categoria.

### Conta
- `adicionar_conta(conta, desc_conta=None)`: Adiciona uma nova conta.
- `listar_contas()`: Lista todas as contas.
- `atualizar_conta(idconta, nova_conta, nova_desc=None)`: Atualiza uma conta existente.
- `remover_conta(idconta)`: Remove uma conta.

### Usuários
- `adicionar_usuario(nome_usuario, email_usuario)`: Adiciona um novo usuário.
- `listar_usuarios()`: Lista todos os usuários.
- `atualizar_usuario(idusuarios, novo_nome, novo_email)`: Atualiza um usuário existente.
- `remover_usuario(idusuarios)`: Remove um usuário.

### Finanças
- `adicionar_financa(idcategoria, idconta, idusuarios, descricao, valor)`: Adiciona uma nova transação financeira.
- `listar_financas()`: Lista todas as transações financeiras.
- `atualizar_financa(idfinancas, nova_descricao, novo_valor)`: Atualiza uma transação financeira existente.
- `remover_financa(idfinancas)`: Remove uma transação financeira.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
