from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('',home), # home
    path('sobre/',sobre), # Sobre
    path('contato/',contato) # Contato
]