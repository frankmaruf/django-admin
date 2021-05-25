from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import ProductGenericAPIView, FileUploadView

urlpatterns = [
    path("products", ProductGenericAPIView.as_view(), name="products"),
    path("products/<str:pk>", ProductGenericAPIView.as_view(), name="product"),
    path('upload', FileUploadView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
