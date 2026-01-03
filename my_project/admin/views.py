from my_project.database.models import UserProfile, Category, SubCategory, Product, ProductImage, Review
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_name]


class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.subcategory_name]


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.product_name, Product.product_type]


class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.id, ProductImage.image]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.comment]
