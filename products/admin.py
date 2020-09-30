from django.contrib import admin
from django.utils.html import format_html
from .models import ( Product,
                      ProductCategories,
                      ProductColor,
                      ProductImage,
                      ProductSize,
                      ProductSubCategories)


class ImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="70px" />'.format(obj.image.url))
    image_tag.short_description = 'Image'

    list_display = ('name', 'category', 'sub_category', 'feature_product', 'best_selling', 'image_tag')
    search_fields = ('name', 'category', 'sub_category',)
    list_filter = ('category', 'sub_category', 'feature_product')
    list_select_related = ('category', 'sub_category')
    list_editable = ('feature_product', 'best_selling')
    inlines = (ImageInline,)
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('category', 'sub_category')


@admin.register(ProductCategories)
class AdminProductCategories(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductColor)
class AdminProductColor(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)
    list_editable = ('code',)


@admin.register(ProductSubCategories)
class AdminProductSubCategories(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductSize)
class AdminProductSize(admin.ModelAdmin):
    list_display = ('size',)

