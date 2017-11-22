from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item, User


engine = create_engine('sqlite:///inventory.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create admin
user1 = User(name="admin", email="admin@localhost.com", admin=True)
session.add(user1)
session.commit()
print('user1 added')


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

item2 = Item(title="Apache Gold and Yaqui Silver", category=category2, author="Dobie, J. Frank", price="90")
session.add(item2)
session.commit()

item3 = Item(title="Earl Vandale on the Trail of Texas Books", category=category2, author="Haley, J. Evetts", price="100")
session.add(item3)
session.commit()

item4 = Item(title="Tickets. To All Going to Kansas, Colorado", category=category3, author="Cowgill & Parsons", price="45")
session.add(item4)
session.commit()

item5 = Item(title="$300 Reward for Mike Baker", category=category3, author="Timmons, J.W.", price="125")
session.add(item5)
session.commit()

item6 = Item(title="Sixteenth Annual Interstate Thresher and Tractor Show", category=category2, author="Wichita Eagle Press", price="150")
session.add(item6)
session.commit()

item7 = Item(title="The Best Thing in the West Rich Valley", category=category3, author="Santa Fe Railroad", price="600")
session.add(item7)
session.commit()

item8 = Item(title="Ben Kuroki's Story", category=category2, author="Kuroki, Ben", price="75")
session.add(item8)
session.commit()

item9 = Item(title="A Lady at Camp No 2 Pacific Railroad", category=category4, author="Lady to Mr. Hope", price="300")
session.add(item9)
session.commit()

item10 = Item(title="American News - Extra. Telegraphic Dispatch", category=category6, author="Library of Congress", price="225")
session.add(item10)
session.commit()

item11 = Item(title="Map of the Richmond and Louisville Railroad", category=category5, author="Colton, G.W.", price="100")
session.add(item11)
session.commit()

item12 = Item(title="Map of Texas", category=category5, author="Ikin, Arthur", price="2250")
session.add(item12)
session.commit()

item13 = Item(title="Millions of Acres Iowa and Nebraska Lands for Sale", category=category7, author="Burlington & Missouri River R.R.", price="775")
session.add(item13)
session.commit()

item14 = Item(title="Kansas Lands Low Prices Long Time", category=category7, author="Atchison Topeka and Santa Fe", price="1000")
session.add(item14)
session.commit()

item15 = Item(title="Arizona - Rich Hills Gold Mines", category=category8, author="Rich Hills Mines Company", price="1080")
session.add(item15)
session.commit()

item16 = Item(title="G.J. Ayars Coal Mine ", category=category8, author="Ayars, G.J.", price="500")
session.add(item16)
session.commit()


print('Items added!')
