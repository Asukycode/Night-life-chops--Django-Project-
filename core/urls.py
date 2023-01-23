from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path("dashboard/", views.dashboard, name="dashboard_view"),
    path("aboutus/", views.AboutUs, name="AboutUs"),
    path("checkout/", views.checkout, name="checkout_view"),
    # path('update_item/', views.updateItem, name="update_item"),
    path("search_meals/", views.search_meals, name="search_meals"),
    path('add-to-cart/<int:meal_id>/', views.add_to_cart, name='add_to_cart'),
    path("cart/", views.cart_view, name="cart_view")
]
