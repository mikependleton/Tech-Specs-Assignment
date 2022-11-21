from django.urls import path, include
from . import views
from django_project import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", views.create_file, name="upload"),
    path("home/", views.home, name="home"),
    path("readme/", views.readme, name="readme"),
    path("read_file/", views.read_file, name="read_file"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("registration/register/", views.register_request, name="register"),
    path("registration/login/", views.login_request, name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
