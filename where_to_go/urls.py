from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from debug_toolbar.toolbar import debug_toolbar_urls

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_map),
    path('places/<int:place_id>/', views.show_place_detail, name='show_place_detail')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + debug_toolbar_urls()
