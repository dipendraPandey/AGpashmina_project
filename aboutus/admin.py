from django.contrib import admin
from django.utils.html import format_html
from .models import AboutCompany, Team, ContactUs, CompanyLinks, MainFrameContent
# Register your models here.


@admin.register(AboutCompany)
class AdminAboutCompany(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag')
    search_fields = ('title',)


@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('name', 'position', 'phone_number_1', 'phone_number_2', 'image_tag')
    search_fields = ('name', 'position')


@admin.register(ContactUs)
class AdminContactUs(admin.ModelAdmin):
    list_display = ('location', 'phone', 'email')


@admin.register(MainFrameContent)
class AdminMainFrameContent(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('title', 'image_tag')
    search_fields = ('title',)


admin.site.register(CompanyLinks)
