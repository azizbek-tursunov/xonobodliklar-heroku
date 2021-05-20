from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Yangilik

class HomePageView(ListView):
    model = Yangilik
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Yangilik
    template_name = 'article_detail.html'