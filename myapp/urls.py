from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('webdesign/',views.webdesign, name="webdesign"),
    path('digitalmarketing/',views.digitalmarketing, name="digitalmarketing"),
    path('seo/',views.seo,name="seo"),
    path('aboutus/',views.aboutus,name="aboutus"),
]