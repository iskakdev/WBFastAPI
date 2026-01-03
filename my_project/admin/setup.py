from my_project.admin.views import UserProfileAdmin, CategoryAdmin, SubCategoryAdmin, ProductAdmin, ProductImageAdmin, ReviewAdmin
from fastapi import FastAPI
from sqladmin import Admin
from my_project.database.db import engine


def setup_admin(my_project: FastAPI):
    admin = Admin(my_project, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CategoryAdmin)
    admin.add_view(SubCategoryAdmin)
    admin.add_view(ProductAdmin)
    admin.add_view(ProductImageAdmin)
    admin.add_view(ReviewAdmin)
