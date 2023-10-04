from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    # path('/form',views.form),
    path('about/',views.about,name='about'),
    path('registration/',views.registration,name='registration'),


]
