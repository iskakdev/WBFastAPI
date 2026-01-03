from pydantic import BaseModel, EmailStr
from typing import Optional
from .models import StatusChoices
from datetime import date, datetime


class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]


class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    date_registered: date
    status: StatusChoices


class UserLoginSchema(BaseModel):
    username: str
    password: str


class CategoryInputSchema(BaseModel):
    category_image: str
    category_name: str

 
class CategoryOutSchema(BaseModel):
    id: int
    category_image: str
    category_name: str


class SubCategoryInputSchema(BaseModel):
    subcategory_name: str
    category_id: int


class SubCategoryOutSchema(BaseModel):
    id: int
    subcategory_name: str
    category_id: int


class ProductInputSchema(BaseModel):
    product_name: str
    price: int
    article_number: int
    description: str
    product_type: bool
    video: str
    subcategory_id: int


class ProductOutSchema(BaseModel):
    id: int
    product_name: str
    price: int
    article_number: int
    description: str
    product_type: bool
    video: str
    created_date: datetime
    subcategory_id: int


class ProductImageInputSchema(BaseModel):
    image: str
    product_id: int


class ProductImageOutSchema(BaseModel):
    id: int
    image: str
    product_id: int


class ReviewInputSchema(BaseModel):
    comment: str
    stars: int
    user_id: int
    product_id: int


class ReviewOutSchema(BaseModel):
    id: int
    comment: str
    stars: int
    add_comment: datetime
    user_id: int
    product_id: int
