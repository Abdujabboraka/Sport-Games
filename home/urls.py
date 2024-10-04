from django.urls import path
from .views import homepage, select_by_category, add_sport, add_category
urlpatterns = [
    path('', homepage, name='homepage'),
    path('categories/<category_id>/', select_by_category, name='categories'),
    path('add-sport', add_sport, name='add-sport'),
    path('add-category', add_category, name='add-category'),
]