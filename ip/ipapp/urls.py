
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('carwash/',views.carwash,name="carwash"),
    path('bikewash/',views.bikewash,name="bikewash"),
    path('reviews/',views.reviews,name="reviews"),
    path('contact/',views.contact,name="contact"),


    # Auth
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)