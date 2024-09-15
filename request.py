import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from main import Publisher, Book, Shop, Stock, Sale

DSN = ''
engine = sa.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()


publisher_input = input("Введите имя или ID издателя: ")


query = session.query(
    Book.title,
    Shop.name,
    Sale.price,
    Sale.date_sale
).join(Publisher).join(Stock).join(Shop).join(Sale)

# Если ввели число, ищем по ID, иначе по имени
if publisher_input.isdigit():
    results = query.filter(Publisher.id == int(publisher_input)).all()
else:
    results = query.filter(Publisher.name == publisher_input).all()

for title, shop_name, price, date_sale in results:
    print(f"{title} | {shop_name} | {price} | {date_sale.strftime('%d-%m-%Y')}")

session.close()
