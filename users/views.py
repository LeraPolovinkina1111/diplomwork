from django.shortcuts import render


# Create your views here.
def users_cart(request):
    return render(request, 'users/users_cart.html')
