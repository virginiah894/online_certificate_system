from django.urls.resolvers import URLPattern
from . import views
from django.urls import path, include
from django.conf .urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
