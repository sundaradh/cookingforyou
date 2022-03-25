from django.urls import path   

from .views import UserRegister
from . import views
urlpatterns = [

    path('',views.recipeOverview,name='recipeOverview'),
    path('recipe-list/', views.ShowAll, name='recipe-list'),
    path('recipe-detail/<int:pk>/', views.ViewRecipe, name='recipe-detail'),
    path('recipe-create/', views.CreateRecipe, name='recipe-create'),
    path('recipe-update/<int:pk>/', views.updateRecipe, name='recipe-update'),
    path('recipe-delete/<int:pk>/', views.deleteRecipe, name='recipe-delete'),
    path('register/', UserRegister.as_view(), name='register-user'),
]