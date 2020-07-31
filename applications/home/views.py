from django.shortcuts import render
import datetime
from django.views.generic import TemplateView, ListView

class HomeView(TemplateView):
    template_name = "home/home.html"

class HomeListView(ListView):
    template_name = "home/list.html"
    queryset = ['Albert', 'Andrés', 'Vicky', 'Olivia', 'Sergio']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime.date.today()
        context['query'] = self.queryset
        return context