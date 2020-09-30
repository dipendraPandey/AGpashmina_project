from django.db import models
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    limit_mb = 2.0
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


class AboutCompany(models.Model):
    title = models.CharField(max_length=120)
    detail = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/company', validators=[validate_image])

    def __str__(self):
        return self.title

    def clean(self):
        width, height = get_image_dimensions(self.image)
        if width < 300 or width > 1000:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")
        ratio = width/height
        if ratio < 0.8 or ratio > 1.25:
            raise ValidationError("Image ratio invalid ! min-size:300x240, max-size:1000x1250 ")

    class Meta:
        verbose_name = 'Company Detail'
        verbose_name_plural = 'Company Details'


class Team(models.Model):
    name = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    phone_number_1 = models.CharField(max_length=15,)
    phone_number_2 = models.CharField(max_length=15,null=True, blank=True)
    image = models.ImageField(upload_to='about/team', validators=[validate_image])

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
        verbose_name = 'Team Member'
        verbose_name_plural = 'Company Team'


class ContactUs(models.Model):
    location = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Info'


class MainFrameContent(models.Model):
    title = models.CharField(max_length=120)
    detail = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/maincontent')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Main content'
        verbose_name_plural = 'Main content'


class CompanyLinks(models.Model):
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()
    google_link = models.URLField()

    def __str__(self):
        return 'CompanyLinks'

    class Meta:
        verbose_name = 'links'
        verbose_name_plural = 'Company links'
