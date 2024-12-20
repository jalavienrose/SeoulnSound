import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import ShopEntryForm
from main.models import Shop
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json

@login_required(login_url='/login')
def show_main(request):
    context = {
        'name': request.user.username,
        'pbp_class': "PBP A",
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_shop_entry(request):
    form = ShopEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        shop_entry = form.save(commit=False)
        shop_entry.user = request.user
        shop_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_shop_entry.html", context)

def show_xml(request):
    data = Shop.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Shop.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Shop.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Shop.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_shop(request, id):
    # Get shop entry berdasarkan id
    shop = Shop.objects.get(pk = id)

    # Set shop entry sebagai instance dari form
    form = ShopEntryForm(request.POST or None, instance=shop)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_shop.html", context)

def delete_shop(request, id):
    # Get shop berdasarkan id
    shop = Shop.objects.get(pk = id)
    # Hapus shop
    shop.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_shop_entry_ajax(request):
    product_name = strip_tags(request.POST.get("product_name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    rating = request.POST.get("rating")
    user = request.user

    new_shop = Shop(
        product_name=product_name, price=price, description=description, rating=rating, user=user
    )
    new_shop.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Shop.objects.create(
            user=request.user,
            product_name=data["product_name"],
            price=int(data["price"]),
            description=data["description"],
            rating=int(data["rating"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)