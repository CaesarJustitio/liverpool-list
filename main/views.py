from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from main.models import Item
from django.contrib import messages

# Create your views here.
def show_main(request):
    items = Item.objects.all()

    context = {
        'name': 'Caesar Justitio',
        'class': 'PBP E',
        'appname': 'Liverpoolist',
        'position1': 'Goalkeeper',
        'position2': 'Defender',
        'position3': 'Midfielder',
        'position4': 'Attacker',
        'items': items
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()

        players = Item.objects.count()

        messages.success(request, f"Kamu berhasil menyimpan {players} pemain pada liverpoolist. You'll Never Walk Alone")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")