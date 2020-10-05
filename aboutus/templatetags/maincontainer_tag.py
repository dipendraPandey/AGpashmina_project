from django import template
from ..models import MainFrameContent
from aboutus.models import CompanyLinks,ContactUs

register = template.Library()


@register.inclusion_tag('aboutus/main_content_tag/main_image_content.html')
def main_frame_content():
    maincontent= MainFrameContent.objects.all()[:1]
    return {'maincontent': maincontent}


@register.inclusion_tag('snippets/footer.html')
def footer_content():
    contact = ContactUs.objects.last()
    links = CompanyLinks.objects.last()
    return {'contact': contact,
            'links': links}
