from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#localhost:8000/Work
urlpatterns = [
    path('',views.Work, name='myWork'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)