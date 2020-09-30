from django import template
from ..models import MainFrameContent

register = template.Library()


@register.inclusion_tag('aboutus/main_content_tag/main_image_content.html')
def main_frame_content():
    maincontent= MainFrameContent.objects.all()[:1]
    return {'maincontent': maincontent}
