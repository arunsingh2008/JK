


from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', published_date='{self.published_date}')>"


