import pyodbc
import time
from config import Config

def get_db_connection():
    """Estabelece conexão com o banco de dados"""
    try:
        print(f"Tentando conectar em: {Config.DB_SERVER}")
        print(f"Database: {Config.DB_DATABASE}")
        print(f"Usuário: {Config.DB_USERNAME}")
        
        conn = pyodbc.connect(Config.DB_CONNECTION_STRING)
        print("✅ Conexão estabelecida com sucesso!")
        return conn
    except pyodbc.Error as e:
        print(f"❌ Erro ao conectar com o banco: {e}")
        print("String de conexão (sem senha):", Config.DB_CONNECTION_STRING.replace(Config.DB_PASSWORD, "****"))
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

def test_connection():
    """Testa a conexão com o banco"""
    print("🔍 Testando conexão...")
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT @@version, GETDATE()")
            result = cursor.fetchone()
            print(f"✅ Conexão OK! Versão: {result[0][:50]}...")
            print(f"📅 Data/Hora servidor: {result[1]}")
            conn.close()
            return True
        except Exception as e:
            print(f"❌ Erro ao executar query de teste: {e}")
            return False
    return False

def init_db():
    """Inicializa o banco de dados"""
    print("🚀 Inicializando banco de dados...")
    
    # Primeiro, tentar conectar sem especificar database para criar o banco
    try:
        conn = pyodbc.connect(Config.DB_CONNECTION_STRING_NO_DB)
        cursor = conn.cursor()
        
        # Verificar se database existe
        cursor.execute("SELECT name FROM sys.databases WHERE name = ?", (Config.DB_DATABASE,))
        if not cursor.fetchone():
            print(f"📝 Criando database {Config.DB_DATABASE}...")
            cursor.execute(f"CREATE DATABASE {Config.DB_DATABASE}")
            print("✅ Database criado!")
        else:
            print(f"✅ Database {Config.DB_DATABASE} já existe")
        
        conn.close()
        
        # Agora conectar ao database específico
        time.sleep(1)  # Aguardar um momento
        conn = get_db_connection()
        if not conn:
            print("❌ Não foi possível conectar ao database")
            return False
            
        cursor = conn.cursor()
        
        # Criar tabela usuario
        print("📝 Criando tabela usuario...")
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='usuario' AND xtype='U')
            CREATE TABLE usuario (
                id_usuario int primary key identity (1,1) not null,
                nome varchar (255) not null,
                sobrenome varchar (255) not null,
                e_mail varchar (100) not null unique,
                telefone varchar (20) not null
            )
        """)
        
        # Criar tabela pet
        print("📝 Criando tabela pet...")
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='pet' AND xtype='U')
            CREATE TABLE pet (
                id_pet int primary key identity (1,1) not null,
                nome varchar(100) null,
                especie varchar (30) not null check (especie in ('Cachorro', 'Gato', 'Outros')),
                raca varchar(100) null,
                situacao varchar (15) not null check (situacao in ('Achado', 'Perdido')),
                foto VARCHAR(255) NULL,
                data date not null,
                sexo varchar (15) not null check (sexo in ('Macho', 'Fêmea')),
                descricao varchar(max) not null,
                mensagem_dono varchar(max) null,
                nome_tutor varchar(255) not null,
                telefone_tutor varchar(20) not null,
                visto_em varchar(255) not null, -- Este campo será usado para a localização completa
                id_usuario INT NOT NULL,
                foreign key (id_usuario) references usuario (id_usuario)
            )
        """)
        
        conn.commit()
        conn.close()
        print("✅ Banco inicializado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Executando testes de conexão...")
    if test_connection():
        print("🚀 Tentando inicializar banco...")
        init_db()
    else:
        print("❌ Falha nos testes de conexão")