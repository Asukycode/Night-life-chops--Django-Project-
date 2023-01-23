from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import request
from core.models import Meal
from django.http import JsonResponse
# Create your views here.
app_name = "core"
def landing_page(request):
    # slides = Slide.objects.all()
    # context = {'slides': slides}
    
    return render(request, "index.html")

def dashboard(request):
    meal = Meal.objects.all()
    context = {
        "meals":meal
    }
    return render(request, "dashboard.html", context)

def AboutUs(request):
    return render(request, 'AboutUs.html')



def add_to_cart(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    cart = request.session.get('cart', [])
    cart.append(meal.id)
    request.session['cart'] = cart
    return redirect(reverse('core:cart_view'))

def cart_view(request):
    cart = request.session.get('cart', [])
    meals = Meal.objects.filter(id__in=cart)
    context = {'meals': meals}
    return render(request, 'shoppingcart.html', context)
    
def checkout(request):
    return render(request, 'checkout.html')


# def  updateItem(request):
#     return JsonResponse("Item Was added", safe=False)

def search_meals(request):
    if request.method == "POST":
        searched_meal = request.POST['searched_meal']
        meal = Meal.objects.filter(name__contains=searched_meal)
        context = {
                "searched_meal":searched_meal,
                'meals':meal
            }
        return render(request, "search_meals.html", context)    
    else:

        context = {
        }
        return render(request, "search_meals.html", context)

