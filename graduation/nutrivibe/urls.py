from django.urls import path, include
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('nutrition_plan', NutritionPlanPage.as_view(), name='nutrition_plan'),
    path('checkout_page', CheckoutPage.as_view(), name='checkout_page'),
    path('products', ProductsPage.as_view(), name='products'),
    path('product', SingleProduct.as_view(), name='product'),
    path('bmi_calculator', BMICalculator.as_view(), name='bmi_calculator'),
    path('exercises', ExercisesPage.as_view(), name='exercises'),
    path('recipes', RecipesPage.as_view(), name='recipes'),
    path('recipe_detail', RecipesDetailsPage.as_view(), name='recipe_detail'),
    path('user_orders', UserOrdersHandler().get_user_orders, name='user_orders'),
    path('order_details', UserOrdersHandler().show_one_order, name='order_details'),
    path('add_to_cart', UserCartHandler().add_item_to_cart, name='add_to_cart'),
    path('place_order', UserCartHandler().place_order, name='place_order'),
    path('remove_from_cart', UserCartHandler().remove_from_cart, name='remove_from_cart'),
    path('user_cart', UserCartHandler().get_user_cart, name='user_cart'),
    path('user_choices', UserProfileHandler().choices_page, name='user_choices'),
    path('user_profile', UserProfileHandler().user_profile, name='user_profile'),
]
