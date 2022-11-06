from django.urls import path
from . import views
from django_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", views.create_file, name="upload"),
    path("home/", views.home, name="home"),
    path("readme/", views.readme, name="readme"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
