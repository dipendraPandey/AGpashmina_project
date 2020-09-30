from django.contrib import admin
from django.utils.html import format_html
from .models import CarouselTrending, CarouselLatest, OurProduct, Contact
# Register your models here.


@admin.register(CarouselLatest)
class AdminCarouselLatest(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ('title', 'image_tag')
    search_fields = ('title',)


@admin.register(CarouselTrending)
class AdminCarouselTrending(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag')
    search_fields = ('title',)


@admin.register(OurProduct)
class AdminOurProduct(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag')
    search_fields = ('title',)


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'email')