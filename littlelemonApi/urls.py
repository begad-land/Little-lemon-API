
from django.urls import path
from .import views


urlpatterns = [
    path('menu-items' , views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>' , views.DestroyUpdateMenuItem.as_view())
    
]
