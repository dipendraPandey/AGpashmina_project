from django.db import models
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    limit_mb = 2.0
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


class CarouselHome(models.Model):
    title = models.CharField(max_length=120, blank=False)
    image = models.ImageField(upload_to='home/carousel_latest/', validators=[validate_image], blank=False)

    def __str__(self):
        return self.title

    def clean(self):
        if self.image == '':
            raise ValidationError("")
        width, height = get_image_dimensions(self.image)
        if width < 300 or width > 1400:
            raise ValidationError("Image width invalid ! min-width:300 , max-width:1200")

        if height < 450 or height > 700:
            raise ValidationError("Image height invalid! min-height:300 , max-height:1200")


class OurProduct(models.Model):
    title = models.CharField(max_length=120)
    detail = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='home/our_product', validators=[validate_image])

    def __str__(self):
        return self.title

    def clean(self):
        if self.image == '':
            raise ValidationError("")
        width, height = get_image_dimensions(self.image)
        if width < 300 or width > 1000:
            raise ValidationError("Image width invalid ! min-width:300 , max-width:1200")

        if height < 300 or height > 1200:
            raise ValidationError("Image height invalid! min-height:300 , max-height:1200")

        ratio = width / height
        if ratio < 0.65 or ratio > 1.25:
            raise ValidationError("Image ratio invalid ! min-ratio:0.65 : max-ratio:1.25")


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact forms'
