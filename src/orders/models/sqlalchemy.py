from datetime import datetime
from decimal import Decimal
from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.types import Enum as SQLEnum

from src.common.databases.postgres import Base


class BasketStatus(str, Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"


class OrderStatus(str, Enum):
    OPEN = "Open"
    PAID = "Paid"
    SENT = "Sent"
    RECEIVED = "Received"
    CANCELLED = "Cancelled"
    RETURNED = "Returned"


class Basket(Base):
    __tablename__ = 'baskets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    price = Column(Numeric(10, 2))
    status = Column(SQLEnum(BasketStatus), default=BasketStatus.OPEN)
    
    lines = relationship('BasketLine', back_populates='basket')
    orders = relationship('Order', back_populates='basket')


class BasketLine(Base):
    __tablename__ = 'basket_lines'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    
    product = relationship('Product')
    basket = relationship('Basket', back_populates='lines')


class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, default=10000)
    basket_id = Column(Integer, ForeignKey('baskets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    total_price = Column(Numeric(10, 2))
    shipping_price = Column(Numeric(10, 2))
    shipping_method = Column(String, nullable=True)
    status = Column(SQLEnum(OrderStatus), default=OrderStatus.OPEN)
    additional_info = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    basket = relationship('Basket', back_populates='orders')
    lines = relationship('OrderLine', back_populates='order')


class OrderLine(Base):
    __tablename__ = 'order_lines'
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    
    product = relationship('Product')
    order = relationship('Order', back_populates='lines')