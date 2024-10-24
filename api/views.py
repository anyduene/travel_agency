from django.shortcuts import render

# views.py
from rest_framework import viewsets
from .models import Hotel
from .repositories.hotel import HotelRepository
from .serializers import HotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


from django.shortcuts import render, get_object_or_404
from .models import Hotel
from django.http import HttpResponseRedirect
from django.urls import reverse

# Виведення списку готелів
def hotel_list(request):
    hotels = HotelRepository.all()
    return render(request, 'hotel_list.html', {'entities': hotels, 'entity_name': 'Hotels'})

# Виведення одного готелю за ID
def hotel_detail(request, hotel_id):
    hotel = HotelRepository.get(hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

# Додавання нового готелю
def add_hotel(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        country = request.POST['country']
        star_rating = request.POST['star_rating']
        mobile_phone = request.POST['mobile_phone']
        site = request.POST['site']

        HotelRepository.create(
            name=name,
            address=address,
            city=city,
            country=country,
            star_rating=star_rating,
            mobile_phone=mobile_phone,
            site=site
        )
        return HttpResponseRedirect(reverse('hotel-list'))

    return render(request, 'add_hotel.html')

