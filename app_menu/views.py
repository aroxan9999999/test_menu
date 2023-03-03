from django.shortcuts import render
from .models import *


def page_1_view(request):
    menu = Menu.objects.prefetch_related('menu').filter(page__name='page_1')
    return render(request, template_name='index.html', context={"object": menu})


def page_2_view(request):
    menu = Menu.objects.prefetch_related('menu').select_related('page').filter(page__name='page_2')
    return render(request, template_name='index.html', context={"object": menu})


def page_3_view(request):
    menu = Menu.objects.prefetch_related('menu').select_related('page').filter(page__name='page_3')
    return render(request, template_name='index.html', context={"object": menu})
