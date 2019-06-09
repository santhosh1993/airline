from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Flight,Passengers

def index(request):
    context={
        "flights":Flight.objects.all(),
        "passengers":Passengers.objects.all()
    }

    return render(request,"flights/index.html",context)

def flight(request,flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight Doesnot exist.")

    context={
        "flight":flight,
        "passengers":flight.passengers.all(),
        "non_passengers":Passengers.objects.exclude(flights=flight).all()
    }

    return render(request,"flights/flight.html",context)

def book(request,flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passengers.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request,"flights/error.html",{"message":"No Selected Passenger"})
    except Flight.DoesNotExist:
        return render(request,"flights/error.html",{"message":"No Flight exists"})
    except Passenger.DoesNotExist:
        return render(request,"flights/error.html",{"message":"No Passenger exists"})

    passenger.flights.add(flight)

    return HttpResponseRedirect(reverse("flight_details",args=(flight_id,)))
