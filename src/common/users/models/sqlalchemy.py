from datetime import datetime

from src.common.databases.postgres import Base
from sqlalchemy import(Column, Integer, String, DateTime, Boolean, ForeignKey)
from sqlalchemy.orm import relationship



class User(Base):
    id= Column(Integer, primary_key=True, index=True)
    email= Column(String, unique=True, index=True)
    phone= Column(String, unique=True, index=True)
    is_admin= Column(Boolean, default=False)
    is_active= Column(Boolean, default=True)
    hashed_password= Column(String)
    first_name= Column(String)
    date_joined= Column(DateTime, default=datetime.datetime.now(tz=datetime.timezone.utc))
    last_login=Column(DateTime, nullable=True)
    addresses=relationship('UserAddress', back_populates='user')


    def __str__(self):
        return f'User: {self.email}'



class UserAddress(Base)
    __tablename__='user_addresses'
    id=Column(Integer, primary_key=True, index= True)
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    title=Column(String, nullable=True)
    city=Column(String)
    street=Column(String)
    apartment=Column(String, nullable=True)
    post_code=Column(String, nullable=True)
    additional_info=Column(String, nullable=True)

    user=relationship('User', back_populates='addresses')