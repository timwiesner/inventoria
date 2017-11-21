from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item


engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="Archives")
session.add(category1)
session.commit()

category2 = Category(name="Books")
session.add(category2)
session.commit()

category3 = Category(name="Broadsides")
session.add(category3)
session.commit()

category4 = Category(name="Letters")
session.add(category4)
session.commit()

category5 = Category(name="Maps")
session.add(category5)
session.commit()

category6 = Category(name="Newspapers")
session.add(category6)
session.commit()

category7 = Category(name="Pamphlets")
session.add(category7)
session.commit()

category8 = Category(name="Photographs")
session.add(category8)
session.commit()

print('Categories Added!')


item1 = Item(title="Six Watercolor Paintings", category=category1, author="Shaw, Charles", price="1000")
session.add(item1)
session.commit()

print('Items added!')
