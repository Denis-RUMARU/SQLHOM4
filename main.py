import sqlalchemy as sa
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    books = relationship("Book", back_populates="publisher")


class Book(Base):
    __tablename__ = 'book'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship("Publisher", back_populates="books")
    stocks = relationship("Stock", back_populates="book")


class Shop(Base):
    __tablename__ = 'shop'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)

    stocks = relationship("Stock", back_populates="shop")


class Stock(Base):
    __tablename__ = 'stock'

    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'), nullable=False)
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)

    book = relationship("Book", back_populates="stocks")
    shop = relationship("Shop", back_populates="stocks")
    sales = relationship("Sale", back_populates="stock")


class Sale(Base):
    __tablename__ = 'sale'

    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Numeric, nullable=False)
    date_sale = sa.Column(sa.Date, nullable=False)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'), nullable=False)
    count = sa.Column(sa.Integer, nullable=False)

    stock = relationship("Stock", back_populates="sales")




