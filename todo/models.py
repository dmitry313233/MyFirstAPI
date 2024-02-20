from sqlalchemy.orm import Mapped, mapped_column

from todo.database.base import Base, engine


class ToDo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]
    is_complete: Mapped[bool] = mapped_column(default=False)

Base.metadata.create_all(bind=engine)

    # РАВНОЗНАЧНО ЭТОМУ КОДУ

# class ToDo(Base):
#     __tablename__ = 'todos'
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     is_completed = Column(Boolen, default=False)