from django.shortcuts import render
from .models import Team, AboutCompany, ContactUs
from django.views.generic import ListView
# Create your views here.


class AboutUsView(ListView):
    template_name = 'aboutus/aboutus.html'
    context_object_name = 'team'

    def get_queryset(self):
        self.teams = Team.objects.all()
        return self.teams

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_company'] = AboutCompany.objects.all()
        return context
