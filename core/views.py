from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader

from .models import Plant_info, Seed_inventory
from .functions import find_entries_in_date_range
from .forms import DateFilterForm
from datetime import datetime
from collections import defaultdict


# Create your views here.
def index(request):
    latest_plants_list = Plant_info.objects.order_by("-pub_date")[:10]
    template = loader.get_template("core/index.html")
    context = {"latest_plants_list": latest_plants_list}
    return HttpResponse(template.render(context, request))


def all_plants(request):
    plant_list = Plant_info.objects.order_by("plant_name")
    template = loader.get_template("core/all_plants.html")
    context = {"plant_list": plant_list}
    return HttpResponse(template.render(context, request))


# def detail(request, plant_info_id):
#    # output = "\n".join
#    plant_info = Plant_info.objects.filter(id=plant_info_id)
#    template = loader.get_template("core/plantinfo.html")
#    context = {"plant_info": plant_info}
#    return HttpResponse(template.render(context, request))
# return HttpResponse("you're looking at plant variety %s" % plant_info_id)


def detail(request, plant_info_id):
    plant_info = get_object_or_404(Plant_info, id=plant_info_id)
    variety_list = Seed_inventory.objects.filter(plant_name_id=plant_info_id)
    context = {"plant_info": plant_info, "variety_list": variety_list}
    return render(request, "core/plantinfo.html", context)


def seedinfo(request, seed_info_id):
    seed_info = get_object_or_404(Seed_inventory, id=seed_info_id)
    variety_list = Seed_inventory.objects.filter(plant_name=seed_info.plant_name)
    context = {"seed_info": seed_info, "variety_list": variety_list}
    return render(request, "core/seedinfo.html", context)


def varieties(request, plant_info_id):
    response = "You're looking at all varieties in your seed inventory that match plant type %s."
    plant_info = get_object_or_404(Plant_info, id=plant_info_id)
    variety_list = Seed_inventory.objects.filter(plant_name_id=plant_info_id)
    template = loader.get_template("core/varieties.html")
    context = {"plant_info": plant_info, "variety_list": variety_list}
    return HttpResponse(template.render(context, request))


def all_seeds(request):
    all_seeds = Seed_inventory.objects.all().order_by("plant_name")
    grouped_seeds = defaultdict(list)
    for seed in all_seeds:
        grouped_seeds[seed.plant_name].append(seed)
    return render(request, "core/all_seeds.html", {"all_seeds": dict(grouped_seeds)})


def vote(request, plant_info_id):
    return HttpResponse("you're voting on plant_info %s." % plant_info_id)


def plantnow(request):
    selected_date = timezone.now()
    if request.GET.get("plant_now_date"):
        try:
            selected_date = datetime.strptime(
                request.GET.get("plant_now_date"), "%Y-%m-%d"
            )
        except:
            pass

    indoor_seeding_now = find_entries_in_date_range(
        Plant_info, "YVR_in_seedDate_start", "YVR_in_seedDate_stop", selected_date
    )
    transplant_now = find_entries_in_date_range(
        Plant_info, "YVR_tpDate_start", "YVR_tpDate_stop", selected_date
    )
    outdoor_seeding_now = find_entries_in_date_range(
        Plant_info, "YVR_out_seedDate_start", "YVR_out_seedDate_stop", selected_date
    )
    return render(
        request,
        "core/plantnow.html",
        {
            "indoor_seeding_now": indoor_seeding_now,
            "transplant_now": transplant_now,
            "outdoor_seeding_now": outdoor_seeding_now,
            "selected_date": selected_date,
        },
    )
