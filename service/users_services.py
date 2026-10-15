from model.users_model import User, UserModel
from utils.security import hash_password

SENHA_TAMANHO_MIN = 8

TAMANHO_MAX_USERNAME = 100

def validate_password(data):
    senha = str(data.get('password' or ""))
    
    if not senha.strip():
        raise ValueError("A senha é obrigatória")
    
    if len(senha) < SENHA_TAMANHO_MIN:
        raise ValueError(f"A senha deve ter no mínimo {SENHA_TAMANHO_MIN} caracteres")
    
    confirmacao = str(data.get('password_confirm') or "")
    
    if not confirmacao:
        raise ValueError("A confirmação é obrigatória")
    
    if senha != confirmacao:
        raise ValueError("As senhas devem ser iguais")
    
    return senha

class UserService:
    @staticmethod
    def get_all():
        try:
            users = UserModel.get_all()
            
            return users
        except Exception as e:
            raise Exception(str(e))
        
    @staticmethod
    def get_by_username(username):
        try:
            user = UserModel.get_by_username(username)
            
            return user
        except Exception as e:
            raise Exception(str(e))
        
    @staticmethod
    def get_by_id(user_id):
        try:
            user = UserModel.get_by_id(user_id)
            
            return user
        except Exception as e:
            raise Exception(str(e))
        
    #POST user
    @staticmethod
    def create(data):
        try:
            if not data:
                raise ValueError("Nenhum dado foi recebido para o usuário")
            
            name = (data.get('name') or '').strip()
            password = data.get('password') or ''
            email = data.get('email') or ''
            fone = data.get('fone') or ''
            
            if not name:
                raise ValueError("O nome é obrigatório")
            
            if len(name) > TAMANHO_MAX_USERNAME:
                raise ValueError(f"O tamanho máximo da senha é de {TAMANHO_MAX_USERNAME} caracteres")
            
            if len(password) < SENHA_TAMANHO_MIN:
                raise ValueError(f"A senha deve ter no mínimo {SENHA_TAMANHO_MIN} caracteres.")
            
            if not email:
                raise ValueError("O usuário tem que digitar um email.")
            
            if not fone:
                raise ValueError("O usuário tem que digitar um telefone")
            
            if UserModel.get_by_username(name):
                raise ValueError("Já existe um usuário com esse nome")
            
            password_hash = hash_password(password)
            
            return UserModel.create(name, password_hash, email, fone)
        except Exception as e:
            raise Exception(str(e))
        
    @staticmethod
    def delete(user_id):
        try:
            if not user_id:
                raise ValueError("O ID do usuário é obrigatório")
            
            if not UserModel.get_by_id(user_id):
                raise ValueError("Nenhum dado foi recebido para o usuário")
            
            return UserModel.delete(user_id)
        except Exception as e:
            raise Exception(str(e))
        
    @staticmethod
    def update(data, id):
        try:            
                        
            if not id:
                raise ValueError("Nenhum ID foi informado")
            
            if not data:
                raise ValueError("Nenhum dado foi recebido para o usuário")
            
            name = (data['new_name'] or '').strip()
            password = data['new_password'] or ''
            email = data['new_email'] or ''
            fone = data['new_fone'] or ''
            
            if not name:
                raise ValueError("Nome não foi enviado")
            
            if not password:
                raise ValueError("Senha não foi enviado")
            
            if not email:
                raise ValueError("Email não foi enviado")
            
            if not fone:
                raise ValueError("Telefone não foi enviado")
            
            password_hash = hash_password(password)
            
            return UserModel.update(name, password_hash, email, fone, id)
        except Exception as e:
            raise Exception(str(e))