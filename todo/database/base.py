import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from todo.config import settings

Base = declarative_base()

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
db_path = os.path.join(BASE_DIR, 'todo', 'database', 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)


engine = create_engine(settings.db_url, connect_args={'check_same_thread': False}, echo=True)  # Создаём движок   Я ТАК ПОНЯЛ ЧТО МЫ РАБОТАЕМ С SQLITE(ПРОВЕРИТЬ)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # bind - объединяем, подключаем локальные сессии с движком


def get_db():   # Интересное подключение, в проекте DeleteProgect мы писали через DABASE_URL
    db_session_local = SessionLocal()
    try:
        yield db_session_local
    finally:
        db_session_local.close()




