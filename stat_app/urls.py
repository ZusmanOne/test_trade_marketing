from django.urls import path
from .views import StatisticListRange, StatisticViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('statistics', StatisticViewSet, basename='statistics')
urlpatterns = router.urls

urlpatterns += [
    path('<str:from_to>/<str:end_to>/', StatisticListRange.as_view()),
]