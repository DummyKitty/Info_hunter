from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet

router = DefaultRouter()
router.register('questions',QuestionViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/',include(router.urls))
]
