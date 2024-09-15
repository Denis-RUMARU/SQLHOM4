import json
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from main import Publisher, Book, Shop, Stock, Sale


DSN = ''
engine = sa.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()


with open('fixtures/tests_data.json', 'r') as f:
    data = json.load(f)


for record in data:
    model_class = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record['model']]
    session.add(model_class(id=record['pk'], **record['fields']))

session.commit()
session.close()
