from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item


engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


item1 = Item(title="Six Watercolor Paintings", category="1", author="Shaw, Charles", price="1000")
session.add(item1)
session.commit()

print('Items added!')
