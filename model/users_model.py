from database.connection_db import get_db_connection

class User:
    def __init__(self, name, email, fone, password_hash, is_active=True, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.fone = fone
        self.password_hash = password_hash
        self.is_active = is_active
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "fone": self.fone,
            "is_active": self.is_active    
        }
        
class UserModel:
    #função get de todos os usuarios cadastrados
    @staticmethod
    def get_all():
        conn = None
        cursor = None
        
        try:
            conn, cursor = get_db_connection()
            
            sql = """
                SELECT id, name, password_hash, email, fone, is_active 
                FROM users
            """
            cursor.execute(sql)
            
            usersData = cursor.fetchall()

            users = [
                User(**user)
                for user in usersData
            ]
            
            return users
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()
            if cursor:
                cursor.close()

                
    @staticmethod
    def get_by_username(username):
        conn = None
        cusor = None
        
        try:
            conn, cursor = get_db_connection()
            
            sql = """
                SELECT name, email, fone, password_hash, is_active
                FROM users
                WHERE name = %s
            """
            
            #precisa passar a variavel no execute para preencher na query
            cursor.execute(sql, (username,))
            userData = cursor.fetchone()
            
            if not userData:
                return None
            
            user = User(**userData)
            
            return user
        except Exception as e:
            raise Exception(str(e))
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            
    @staticmethod
    def get_by_id(user_id):
            conn = None
            cursor = None
            
            try:
                conn, cursor = get_db_connection()
                
                sql = """
                    SELECT id, name, email, fone, password_hash, is_active 
                    FROM users
                    WHERE id = %s
                """
                
                cursor.execute(sql, (user_id,))
                userData = cursor.fetchone()
                
                if not userData:
                    return None
                
                user = User(**userData)
                
                return user
            except Exception as e:
                raise Exception(str(e))
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()        


    @staticmethod
    def create(name, password_hash, email, fone):
        conn = None
        cursor = None
        
        try:
            conn, cursor = get_db_connection()
            
            sql = """
                INSERT INTO users(name, password_hash, email, fone)
                VALUES(%s, %s, %s, %s)
                RETURNING id, name, password_hash, email, fone, is_active
            """
            
            cursor.execute(sql, (name, password_hash, email, fone))
            userCreate = cursor.fetchone()
            
            conn.commit()
            
            user = User(**userCreate)
            
            return user
        except Exception as e:
            raise Exception(str(e))
        finally:
            if conn:
                conn.close()
            if cursor:
                cursor.close()
                
    @staticmethod
    def update(name, password_hash, email, fone, id):
        conn = None
        cursor = None
        
        try:
            conn, cursor = get_db_connection()
            
            user = name, password_hash, email, fone, id
            
            sql = """
                UPDATE users
                SET name = %s, password_hash = %s, email = %s, fone = %s
                WHERE id = %s
            """
            
            cursor.execute(sql, (user))
            conn.commit()
                       
            return user
        except Exception as e:
            raise Exception(str(e))
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
                
    @staticmethod
    def delete(user_id):
        conn = None
        cursor = None
        
        try:
            conn, cursor = get_db_connection()
            
            sql = """
                DELETE FROM users
                WHERE id = %s
            """
            
            cursor.execute(sql, (user_id,))
            conn.commit()
            
            return True
        except Exception as e:
            raise Exception(str(e))
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()