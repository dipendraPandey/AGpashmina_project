from django.db import models
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
# Create your models here.


class ProductSize(models.Model):
    size = models.CharField(max_length=20)
    name = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class ProductCategories(models.Model):
    name = models.CharField(max_length=200)
    sub_category = models.ManyToManyField("ProductSubCategories", related_name='subcategory')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductSubCategories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


def upload_location_product(instance, filename):
    file_path = 'product/{category}/{name}-{filename}'.format(
        category=str(instance.category), name=str(instance.name), filename=filename)
    return file_path


def validate_image(image):
    file_size = image.file.size
    limit_mb = 2.0
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    detail = models.TextField(max_length=1000)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, related_name='p_category')
    sub_category = models.ForeignKey(ProductSubCategories, on_delete=models.CASCADE, related_name='p_subcategory')
    p_size = models.ManyToManyField(ProductSize, related_name='p_size')
    colors = models.ManyToManyField(ProductColor, related_name='p_colors')
    feature_product = models.BooleanField(default=False)
    best_selling = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_location_product, validators=[validate_image])
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        width, height = get_image_dimensions(self.image)
        if width < 300 or width > 1000:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")
        ratio = width/height
        if ratio < 0.8 or ratio > 1.25:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")



    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-date_created']


def upload_location(instance, filename):
    file_path = 'product/{category}/{name}-{filename}'.format(
        category=str(instance.product.category), name=str(instance.product.name), filename=filename)
    return file_path


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(upload_to=upload_location, validators=[validate_image])

    def __str__(self):
        return str(self.product)

    def clean(self):
        width, height = get_image_dimensions(self.image)
        if width < 300 or width > 1000:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")
        ratio = width/height
        if ratio < 0.8 or ratio > 1.25:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
