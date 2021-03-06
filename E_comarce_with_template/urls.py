
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',include('home_app.urls')),
    path('store',include('store_app.urls')),
    path('cart',include('cart_app.urls')),
    path('authentication',include('authentication_app.urls'))
    #path('store',include(('store_app.urls','store_app'),namespace='store_app')),
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)