import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# class User(Base):
#     __tablename__ = 'user'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250))
    pub_date = Column(Integer)
    pub_city = Column(String(50))
    pub_state = Column(String(25))
    pur_date = Column(Integer)
    price = Column(Integer)
    pur_from = Column(String(50))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'pub_date': self.pub_date,
            'pub_city': self.pub_city,
            'pub_state': self.pub_state,
            'pur_date': self.pur_date,
            'price': self.price,
            'pur_from': self.pur_from,
        }


engine = create_engine('sqlite:///inventory.db')

Base.metadata.create_all(engine)
