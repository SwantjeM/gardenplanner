from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_plants/", views.all_plants, name="all_plants"),
    # ex: /garden_planner/5
    path("<int:plant_info_id>/", views.detail, name="detail"),
    # ex: /garden_planner/5/varieties
    path("<int:plant_info_id>/varieties/", views.varieties, name="varieties"),
    # ex: /garden_planner/5/vote
    path("<int:plant_info_id>/vote/", views.vote, name="vote"),
    path("plantnow", views.plantnow, name="plantnow"),
    path("seedinventory/<int:seed_info_id>", views.seedinfo, name="seedinfo"),
]
