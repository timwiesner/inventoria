from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item


engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="Archive")
session.add(category1)
session.commit()

category2 = Category(name="Book")
session.add(category2)
session.commit()

category3 = Category(name="Broadside")
session.add(category3)
session.commit()

category4 = Category(name="Letter")
session.add(category4)
session.commit()

category5 = Category(name="Map")
session.add(category5)
session.commit()

category6 = Category(name="Newspaper")
session.add(category6)
session.commit()

category7 = Category(name="Pamphlet")
session.add(category7)
session.commit()

category8 = Category(name="Photo")
session.add(category8)
session.commit()

print('Categories Added!')
