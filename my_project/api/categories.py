from fastapi import APIRouter, Depends, HTTPException
from my_project.database.models import Category
from my_project.database.schema import CategoryInputSchema, CategoryOutSchema
from my_project.database.db import SessionLocal
from typing import List
from sqlalchemy.orm import Session

category_router = APIRouter(prefix='/categories', tags=['Categories'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@category_router.post('/', response_model=CategoryOutSchema)
async def create_user(user: CategoryInputSchema, db: Session = Depends(get_db)):
    category_db = Category(**user.dict())
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db


@category_router.get('/', response_model=List[CategoryOutSchema])
async def list_category(db: Session = Depends(get_db)):
    return db.query(Category).all()


@category_router.get('/{category_id}/', response_model=CategoryOutSchema)
async def detail_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай маалымат жок', status_code=400)

    return category_db


@category_router.put('/{category_id}/', response_model=dict)
async def update_category(category_id: int, category: CategoryInputSchema,
                          db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай категория жок', status_code=400)

    for category_key, category_value in category.dict().items():
        setattr(category_db, category_key, category_value)

    db.commit()
    db.refresh(category_db)
    return {'massage': 'Категория озгорулду'}


@category_router.delete('/{category_id}/', response_model=dict)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай категория жок', status_code=400)

    db.delete(category_db)
    db.commit()
    return {'massage': 'Категория удалить болду'}
