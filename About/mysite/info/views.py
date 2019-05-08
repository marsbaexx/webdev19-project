from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class infoPageView(TemplateView):
    def get(self, request):
        return render(request, 'info.html', context=None)