from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food_item/<int:id>', views.food_item, name='item'),
    path('cart', views.cart, name='cart'),
    path('addcart/<int:id>', views.add_to_cart, name='addcart'),
    path('delete/<int:id>', views.delete_from_cart, name='deletecart'),
    path('add/<int:id>', views.add_qty, name='add'),
    path('remove/<int:id>', views.remove_qty, name='remove'),
]
