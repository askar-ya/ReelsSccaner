from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='Reels Scaner'),
    path('compilations/', views.compilations, name='Compilations'),
    path('compilations/<int:category>', views.compilations),
    path('add_authors/', views.add_authors),
    path('add_authors/add/', views.add_authors_post),
]
