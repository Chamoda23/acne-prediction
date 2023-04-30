from django.urls import path
from . import views

urlpatterns = [
    path('image', views.ImageView.as_view(), name='image')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)