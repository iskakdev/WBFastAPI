from fastapi import FastAPI
from my_project.api import users, categories, subcategories, products, product_images, reviews, auth
from my_project.admin.setup import setup_admin
import uvicorn

wb_app = FastAPI(title='Shop Project')
wb_app.include_router(users.user_router)
wb_app.include_router(categories.category_router)
wb_app.include_router(subcategories.subcategory_router)
wb_app.include_router(products.product_router)
wb_app.include_router(product_images.product_image_router)
wb_app.include_router(reviews.review_router)
wb_app.include_router(auth.auth_router)
setup_admin(wb_app)


if __name__ == '__main__':
    uvicorn.run(wb_app, host='127.0.0.1', port=8000)