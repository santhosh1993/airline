from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="flight_list"),
    path("<int:flight_id>",views.flight,name="flight_details"),
    path("<int:flight_id>/book",views.book,name="flight_booking"),
]
