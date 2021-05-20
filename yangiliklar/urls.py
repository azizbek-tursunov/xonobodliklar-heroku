from django.urls import path
from .views import HomePageView, ArticleDetailView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)