from django.shortcuts import render
from django.http import HttpResponse

from .models import Plant_info, Seed_inventory
from django.template import loader


# Create your views here.
def index(request):
    latest_plants_list = Plant_info.objects.order_by("-pub_date")[:5]
    template = loader.get_template("core/index.html")
    context = {"latest_plants_list": latest_plants_list}
    return HttpResponse(template.render(context, request))


def detail(request, plant_info_id):
    # output = "\n".join
    return HttpResponse("you're looking at plant variety %s" % plant_info_id)


def varieties(request, plant_info_id):
    response = "You're looking at all varieties in your seed inventory that match plant type %s."
    variety_list = Seed_inventory.objects.filter(plant_name_id=plant_info_id)
    template = loader.get_template("core/varieties.html")
    context = {"variety_list": variety_list}
    return HttpResponse(template.render(context, request))


def vote(request, plant_info_id):
    return HttpResponse("you're voting on plant_info %s." % plant_info_id)
