from django.urls import path, include
from Category import views
urlpatterns = [
    path('add/', views.add_category, name="addcategory"),
]