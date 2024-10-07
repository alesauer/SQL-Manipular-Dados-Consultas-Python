
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Categoria(Base):
    """Classe que representa a tabela 'categoria'."""
    __tablename__ = 'categoria'
    idcategoria = Column(Integer, primary_key=True, autoincrement=True)
    desc_categoria = Column(String(255), nullable=False)
    obs_categoria = Column(String(255), nullable=True)

class Conta(Base):
    """Classe que representa a tabela 'conta'."""
    __tablename__ = 'conta'
    idconta = Column(Integer, primary_key=True, autoincrement=True)
    conta = Column(String(255), nullable=False)
    desc_conta = Column(String(255), nullable=True)

class Usuario(Base):
    """Classe que representa a tabela 'usuarios'."""
    __tablename__ = 'usuarios'
    idusuarios = Column(Integer, primary_key=True, autoincrement=True)
    nome_usuario = Column(String(45), nullable=False)
    email_usuario = Column(String(45), nullable=False)

class Financas(Base):
    """Classe que representa a tabela 'financas'."""
    __tablename__ = 'financas'
    idfinancas = Column(Integer, primary_key=True, autoincrement=True)
    idcategoria = Column(Integer, ForeignKey('categoria.idcategoria'), nullable=False)
    idconta = Column(Integer, ForeignKey('conta.idconta'), nullable=False)
    idusuarios = Column(Integer, ForeignKey('usuarios.idusuarios'), nullable=False)
    descricao = Column(String(255), nullable=False)
    valor = Column(Integer, nullable=False)

    categoria = relationship("Categoria")
    conta = relationship("Conta")
    usuario = relationship("Usuario")

DATABASE_URL = "mysql+pymysql://user:password@localhost/financas"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)

# Funções para manipulação de Categoria
def adicionar_categoria(desc_categoria, obs_categoria=None):
    nova_categoria = Categoria(desc_categoria=desc_categoria, obs_categoria=obs_categoria)
    session.add(nova_categoria)
    session.commit()
    return nova_categoria

def listar_categorias():
    return session.query(Categoria).all()

def atualizar_categoria(idcategoria, nova_descricao, nova_obs=None):
    categoria = session.query(Categoria).get(idcategoria)
    if categoria:
        categoria.desc_categoria = nova_descricao
        categoria.obs_categoria = nova_obs
        session.commit()
    return categoria

def remover_categoria(idcategoria):
    categoria = session.query(Categoria).get(idcategoria)
    if categoria:
        session.delete(categoria)
        session.commit()

# Funções para manipulação de Conta
def adicionar_conta(conta, desc_conta=None):
    nova_conta = Conta(conta=conta, desc_conta=desc_conta)
    session.add(nova_conta)
    session.commit()
    return nova_conta

def listar_contas():
    return session.query(Conta).all()

def atualizar_conta(idconta, nova_conta, nova_desc=None):
    conta = session.query(Conta).get(idconta)
    if conta:
        conta.conta = nova_conta
        conta.desc_conta = nova_desc
        session.commit()
    return conta

def remover_conta(idconta):
    conta = session.query(Conta).get(idconta)
    if conta:
        session.delete(conta)
        session.commit()

# Funções para manipulação de Usuario
def adicionar_usuario(nome_usuario, email_usuario):
    novo_usuario = Usuario(nome_usuario=nome_usuario, email_usuario=email_usuario)
    session.add(novo_usuario)
    session.commit()
    return novo_usuario

def listar_usuarios():
    return session.query(Usuario).all()

def atualizar_usuario(idusuarios, novo_nome, novo_email):
    usuario = session.query(Usuario).get(idusuarios)
    if usuario:
        usuario.nome_usuario = novo_nome
        usuario.email_usuario = novo_email
        session.commit()
    return usuario

def remover_usuario(idusuarios):
    usuario = session.query(Usuario).get(idusuarios)
    if usuario:
        session.delete(usuario)
        session.commit()

# Funções para manipulação de Financas
def adicionar_financa(idcategoria, idconta, idusuarios, descricao, valor):
    nova_financa = Financas(
        idcategoria=idcategoria,
        idconta=idconta,
        idusuarios=idusuarios,
        descricao=descricao,
        valor=valor
    )
    session.add(nova_financa)
    session.commit()
    return nova_financa

def listar_financas():
    return session.query(Financas).all()

def atualizar_financa(idfinancas, nova_descricao, novo_valor):
    financa = session.query(Financas).get(idfinancas)
    if financa:
        financa.descricao = nova_descricao
        financa.valor = novo_valor
        session.commit()
    return financa

def remover_financa(idfinancas):
    financa = session.query(Financas).get(idfinancas)
    if financa:
        session.delete(financa)
        session.commit()