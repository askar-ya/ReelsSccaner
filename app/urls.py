from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('search/', views.search_q, name='about'),
    path('add_authors/', views.add_authors),
    path('add_authors/add/', views.add_authors_post),
]
