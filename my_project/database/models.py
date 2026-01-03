from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum, Date, ForeignKey, Text, Boolean, DateTime
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime


class StatusChoices(PyEnum):
    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    simple = 'simple'


class UserProfile(Base):
    __tablename__ = 'wb_profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.simple)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)

    user_review: Mapped[List['Review']] = relationship(back_populates='user',
                                                       cascade='all, delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user',
                                                            cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.first_name}, {self.last_name}'


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('wb_profile.id'))
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    token_user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')


class Category(Base):
    __tablename__ = 'wb_category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    category_image: Mapped[str] = mapped_column(String)
    category_name: Mapped[str] = mapped_column(String, unique=True)

    subcategories: Mapped[List['SubCategory']] = relationship('SubCategory',
                                                               back_populates='category',
                                                               cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.category_name}'


class SubCategory(Base):
    __tablename__ = 'wb_subcategory'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    subcategory_name: Mapped[str] = mapped_column(String, unique=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('wb_category.id'))

    category: Mapped[Category] = relationship(Category, back_populates='subcategories')
    products: Mapped[List['Product']] = relationship(back_populates='subcategory',
                                                     cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.subcategory_name}'


class Product(Base):
    __tablename__ = 'wb_product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(64))
    price: Mapped[int] = mapped_column(Integer)
    article_number: Mapped[int] = mapped_column(Integer, unique=True)
    description: Mapped[str] = mapped_column(Text)
    product_type: Mapped[bool] = mapped_column(Boolean)
    video: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey('wb_subcategory.id'))

    subcategory: Mapped[SubCategory] = relationship(SubCategory, back_populates='products')
    product_images: Mapped[List['ProductImage']] = relationship(back_populates='product',
                                                                cascade='all, delete-orphan')
    product_review: Mapped[List['Review']] = relationship(back_populates='review_product',
                                                          cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.product_name}'


class ProductImage(Base):
    __tablename__ = 'wb_product_image'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String)
    product_id: Mapped[int] = mapped_column(ForeignKey('wb_product.id'))

    product: Mapped[Product] = relationship(Product, back_populates='product_images')


class Review(Base):
    __tablename__ = 'wb_review'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    comment: Mapped[str] = mapped_column(Text)
    stars: Mapped[int] = mapped_column(Integer)
    add_comment: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('wb_profile.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('wb_product.id'))

    user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_review')
    review_product: Mapped[Product] = relationship(Product, back_populates='product_review')

    def __repr__(self):
        return f'{self.comment}'
