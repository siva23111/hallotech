from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

app_name = 'app1'

urlpatterns = [
    path("", views.home, name="h"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.service, name="service"),
    path("Project/", views.project, name="project"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)