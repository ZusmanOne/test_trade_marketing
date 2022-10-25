from django.urls import path
from .views import StatisticListRange, StatisticViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('statistics', StatisticViewSet, basename='statistics')
urlpatterns = router.urls

urlpatterns += [
    path('<str:from_date>/<str:to_date>/', StatisticListRange.as_view()),
]