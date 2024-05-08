from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils import timezone
from .models import *

class HomePage(TemplateView):
    template_name = 'home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Products.objects.filter(stars=5)
        for product in products:
            if product.stars:
                product.stars_range = range(product.stars)
        context['products'] = products
        
        return context

class NutritionPlanPage(LoginRequiredMixin, TemplateView):
    template_name = 'nutritionplan.html'





class ProductsPage(LoginRequiredMixin, TemplateView):
    template_name = 'products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Products.objects.all()
        for product in products:
            if product.stars:
                product.stars_range = range(product.stars)
        context['products'] = products
        
        return context
    
    
class SingleProduct(LoginRequiredMixin, TemplateView):
    template_name = 'single_product.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        product_id = self.request.GET.get('product_id')
        product = Products.objects.filter(id=product_id).first()
        product.stars_range = range(product.stars)
        context['product'] = product
        
        return context


class BMICalculator(TemplateView):
    template_name = 'bmi.html'


class CheckoutPage(TemplateView):
    template_name = 'checkout.html'


class ExercisesPage(TemplateView):
    template_name = 'exercises.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["yoga"] = []
        context["cardio"] = []
        
        all_exersices = Exercises.objects.all()
        for exercise in all_exersices:
            if exercise.type in ["Yoga", "yoga"]:
                context["yoga"].append(exercise)
            else:
                context['cardio'].append(exercise)
                
        return context
    

class RecipesPage(TemplateView):
    template_name = 'recipes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Recipes.objects.all()
        context["recipes"] = recipes
        
        return context


class RecipesDetailsPage(TemplateView):
    template_name = 'recipe_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_id = self.request.GET.get('recipe_id')
        recipe = Recipes.objects.filter(id=recipe_id).first()
        context["recipe"] = recipe
        
        return context
    

class UserOrdersHandler:
    def __init__(self) -> None:
        pass
    
    def get_user_orders(self, request):
        user = request.user
        user_id = user.id

        user_orders = Orders.objects.filter(user_id=user_id).all()
        
        return render(request, 'orders.html', {'user_orders': user_orders})

    def show_one_order(self, request):
        order_id = request.GET.get('order_id')
        
        order = Orders.objects.filter(id=order_id).first()
        
        order_items = OrdersItems.objects.filter(order=order)
        
        for item in order_items:
            item.total_price = item.item.price * item.quantity

        return render(request, 'one_order.html', {'order': order , 'order_items':order_items})
    


class UserProfileHandler:
    def __init__(self) -> None:
        pass
    
    def choices_page(self, request):
        return render(request, 'user_choices.html')
    
    def user_profile(self, request):
        user = request.user
        
        if request.method == 'POST':
            email = request.POST.get('email')
            phone_number = request.POST.get('number')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            print(first_name, last_name)
            # Update user information
            user.email = email
            user.phone_number = phone_number
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile') 
            
        return render(request, 'user_profile.html', {'user': user})



class UserCartHandler:
    def __init__(self) -> None:
        pass
    

    def get_user_cart(self, request):
        user = request.user
        cart_items = UserCartItems.objects.filter(order__user=user)
        cart_subtotal = 0
        for item in cart_items:
            print(item.quantity)
            cart_subtotal += item.item.price * item.quantity
        
        print(cart_subtotal)
        context = {
            'cart_items': cart_items,
            'cart_subtotal': cart_subtotal
            }
        return render(request, 'user_cart.html', context)

    def add_item_to_cart(self, request):
        if request.method == 'POST':
            user = request.user
            item_id = request.POST.get('item_id')
            quantity = int(request.POST.get('quantity', 1))
            
            product = get_object_or_404(Products, id=item_id)

            user_cart, created = UserCart.objects.get_or_create(user=user)
            
            cart_item, created = UserCartItems.objects.get_or_create(order=user_cart, item=product, defaults={'quantity': quantity})
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            return redirect('products')
    
    def remove_from_cart(self, request):
        if request.method == 'POST':
            item_id = request.POST.get('item_id')
            cart_item = get_object_or_404(UserCartItems, id=item_id)
            cart_item.delete()
            return redirect('user_cart')
            
    def place_order(self, request):
        if request.method == 'POST':
            user = request.user
            user_cart = get_object_or_404(UserCart, user=user)
            cart_items = UserCartItems.objects.filter(order=user_cart).all()
            cart_subtotal = 0
            for cart_item in cart_items:
                cart_subtotal += cart_item.item.price * cart_item.quantity
            order = Orders.objects.create(user=user, total_amount=cart_subtotal, order_date=timezone.now())
            
            for cart_item in cart_items:
                
                OrdersItems.objects.create(order=order, item=cart_item.item, quantity=cart_item.quantity)

            user_cart.items.clear()
            print(cart_subtotal)
            return redirect('checkout_page')