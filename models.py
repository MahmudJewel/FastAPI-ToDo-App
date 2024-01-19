from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

