
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Carwash Express"
admin.site.site_title = "Carwash Express"
admin.site.index_title = "Carwash Express"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ipapp.urls')),
    path('home',include('ipapp.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
