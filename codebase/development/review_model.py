


from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    rating = Column(Float, nullable=False)
    comment = Column(String, nullable=True)
    book = relationship('Book', back_populates='reviews')


