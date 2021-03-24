from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "bath",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = ('instant_book', 'host__superuser', 'room_type', 'amenities', 'facilities', 'house_rules', 'city', 'country',)

    search_fields = ('city', '^host__username', )

    filter_horizontal = ('amenities', 'facilities', 'house_rules',)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass