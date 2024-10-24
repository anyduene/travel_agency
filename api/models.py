from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    star_rating = models.IntegerField()
    mobile_phone = models.IntegerField()
    site = models.URLField(null=True, blank=True)

    class Meta:
        db_table = 'Hotel'

    def __str__(self):
        return self.name


class HotelBooking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'HotelBooking'

    def __str__(self):
        return f"Booking for {self.hotel.name} from {self.check_in_date} to {self.check_out_date}"


class Transport(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'Transport'

    def __str__(self):
        return self.type


class TransportBooking(models.Model):
    arrival_date = models.DateField()
    booking_id = models.IntegerField()  # This refers to an external booking system, or you may add a related field
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    place = models.CharField(max_length=255, null=True, blank=True)
    departure_point = models.CharField(max_length=255)
    departure_date = models.DateField()

    class Meta:
        db_table = 'TransportBooking'

    def __str__(self):
        return f"Transport Booking {self.transport.type} from {self.departure_point} on {self.departure_date}"


class Tour(models.Model):
    destination_city = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_booking = models.ForeignKey(HotelBooking, null=True, blank=True, on_delete=models.SET_NULL)
    transport_booking = models.ForeignKey(TransportBooking, null=True, blank=True, on_delete=models.SET_NULL)
    tourist_count = models.IntegerField()

    class Meta:
        db_table = 'Tour'

    def __str__(self):
        return f"Tour: {self.name} to {self.destination_city}, {self.destination_country}"


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True)
    passport_number = models.IntegerField(unique=True, null=True, blank=True)
    nationality = models.CharField(max_length=255)

    class Meta:
        db_table = 'Client'

    def __str__(self):
        return f"{self.name} {self.surname}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Pending', 'Pending'),
        ('Cancelled', 'Cancelled'),
    ]
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Pending')

    class Meta:
        db_table = 'Booking'

    def __str__(self):
        return f"Booking for {self.client} on {self.tour.name} - {self.status}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Cash', 'Cash'),
        ('PayPal', 'PayPal'),
    ]
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Payment'

    def __str__(self):
        return f"Payment of {self.amount} for booking {self.booking.id} by {self.payment_method}"