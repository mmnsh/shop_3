"""from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.article_list),
    path('detail/<int:pk>/', views.article_detail),
]"""

"""
Method 3:
from django.urls import path
from .views import ArticleAPIView, ArticleDetails

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
]"""

"""
Method 4

from django.urls import path
from .views import GenericAPIView

urlpatterns = [

    path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),

]
"""

"""
Method 5
"""

from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls))

]
