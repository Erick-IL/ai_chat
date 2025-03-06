from database.config import Base, session_factory
from dotenv import load_dotenv
from sqlalchemy import Column, String, JSON
import os 

class User(Base):
    load_dotenv()
    __tablename__ = os.getenv('DB_DATABASE')
    id = Column('ID', String(256), nullable=False, primary_key=True)
    user_history = Column(JSON, default=[])


    def __init__(self, id, user_history=None):
        self.id = id
        self.user_history = user_history or []
    
def create_user(user_id, conversation):
    session = session_factory()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        print('Usuário já existe. Atualizando histórico')
        if user.user_history is None: user.user_history = []
        user.user_history.append(conversation)

        session.query(User).filter(User.id == user_id).update(
            {'user_history': user.user_history}
        )
    else:
        print('Usuário não encontrado. Criando novo usuário')
        new_user: User = User(user_id, [conversation])
        session.add(new_user)

    session.commit()
    session.close()
     
def get_user_history(user_id):
    session = session_factory()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user.id, user.user_history
    except Exception as e:
        print('Usuario não encontrado ou não criado:', e)
        return user_id, ""