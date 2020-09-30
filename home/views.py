from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView
from aboutus.models import Team
from .models import CarouselLatest, CarouselTrending, OurProduct
from products.models import Product
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


class HomeView(ListView):
    template_name = 'home/homepage.html'
    context_object_name = 'carousel_latest'

    def get_queryset(self):
        self.carousel_latest = CarouselLatest.objects.all()[:3]
        return self.carousel_latest

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the crousel
        context['carousel_trending'] = CarouselTrending.objects.all().reverse()
        context['feature_product'] = Product.objects.filter(feature_product=True)[:3]
        context['our_product'] = OurProduct.objects.all().reverse()[:3]
        return context


class ContactUsView(CreateView):
    template_name = 'home/contactus.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.team = Team.objects.all()
        self.context['contact_team'] = self.team
        self.context['form'] = ContactForm()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                text_message = form.cleaned_data['message']
                form.save()
                messages.success(request, 'Thank you for Message !')
                send_mail(
                    'Contact form',
                    '{} is trying to contact us Email:{} message{}'.format(name, email,text_message),
                    'agpashmina.info@gmail.com',
                    ['dipendrapandey666@gmail.com'],
                    fail_silently=False,
                )
                self.context['form'] = ContactForm()
                return redirect('contact-us')
            else:
                self.context['form'] = form
                messages.error(request, 'Fail to send message')
                return render(request, self.template_name, self.context)
        return render(request, self.template_name, self.context)





