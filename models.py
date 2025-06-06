from database import get_db_connection

class Usuario:
    def __init__(self, nome, sobrenome, email, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone
    
    def salvar(self):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                sql_query = """
                    INSERT INTO usuario (nome, sobrenome, e_mail, telefone)
                    OUTPUT INSERTED.id_usuario
                    VALUES (?, ?, ?, ?)
                """
                cursor.execute(sql_query, (self.nome, self.sobrenome, self.email, self.telefone))
                result = cursor.fetchone()
                user_id = int(result[0]) if result else None
                conn.commit()
                conn.close()
                return user_id
            except Exception as e:
                print(f"Erro ao salvar usuário: {e}")
                conn.rollback() 
                conn.close()
                return None
        return None
    
    @staticmethod
    def buscar_por_email(email):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM usuario WHERE e_mail = ?", (email,))
                user = cursor.fetchone()
                conn.close()
                return user
            except Exception as e:
                print(f"Erro ao buscar usuário: {e}")
                conn.close()
                return None
        return None

class Pet:
    # ATENÇÃO: __init__ foi alterado
    def __init__(self, nome, especie, raca, situacao, foto, data, sexo, 
                 descricao, mensagem_dono, nome_tutor, telefone_tutor, 
                 visto_em, id_usuario):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.situacao = situacao
        self.foto = foto
        self.data = data
        self.sexo = sexo
        # REMOVIDO: self.cidade e self.bairro
        self.descricao = descricao
        self.mensagem_dono = mensagem_dono
        self.nome_tutor = nome_tutor
        self.telefone_tutor = telefone_tutor
        self.visto_em = visto_em
        self.id_usuario = id_usuario
    
    # ATENÇÃO: salvar() foi alterado
    def salvar(self):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                
                sql_query = """
                    INSERT INTO pet (nome, especie, raca, situacao, foto, data, sexo, 
                                   descricao, mensagem_dono, nome_tutor, telefone_tutor, 
                                   visto_em, id_usuario)
                    OUTPUT INSERTED.id_pet
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """

                # Parâmetros sem cidade e bairro
                params = (self.nome, self.especie, self.raca, self.situacao, self.foto, 
                          self.data, self.sexo, self.descricao,
                          self.mensagem_dono, self.nome_tutor, self.telefone_tutor, 
                          self.visto_em, self.id_usuario)

                cursor.execute(sql_query, params)
                
                result = cursor.fetchone()
                pet_id = int(result[0]) if result else None

                conn.commit()
                conn.close()
                return pet_id
            except Exception as e:
                print(f"Erro ao salvar pet: {e}")
                conn.rollback()
                conn.close()
                return None
        return None
    
    @staticmethod
    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                # CORREÇÃO: Adicionamos DISTINCT para garantir que cada pet apareça apenas uma vez.
                cursor.execute("""
                    SELECT DISTINCT p.id_pet, p.nome, p.especie, p.raca, p.situacao, p.foto, p.data, 
                                    p.sexo, p.descricao, p.mensagem_dono, p.nome_tutor, 
                                    p.telefone_tutor, p.visto_em, p.id_usuario, u.nome as nome_usuario, u.e_mail
                    FROM pet p 
                    JOIN usuario u ON p.id_usuario = u.id_usuario
                    ORDER BY p.data DESC
                """)
                # NOTA: Tive que listar as colunas explicitamente por causa do DISTINCT com ORDER BY.
                pets = cursor.fetchall()
                conn.close()
                return pets
            except Exception as e:
                print(f"Erro ao listar pets: {e}")
                conn.close()
                return []
        return []
    
    @staticmethod
    def buscar_por_id(pet_id):
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT p.*, u.nome as nome_usuario, u.sobrenome, u.e_mail 
                    FROM pet p 
                    JOIN usuario u ON p.id_usuario = u.id_usuario
                    WHERE p.id_pet = ?
                """, (pet_id,))
                pet = cursor.fetchone()
                conn.close()
                return pet
            except Exception as e:
                print(f"Erro ao buscar pet: {e}")
                conn.close()
                return None
        return None