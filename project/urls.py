from django.contrib import admin
from django.urls import path, include
from donatory import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('donatory.urls', namespace='donatory')),
    path('accounts/', include('allauth.urls')),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
