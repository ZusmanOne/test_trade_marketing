from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import StatisticSerializer
from .models import Statistic
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class StatisticListRange(APIView):
    def get(self, request, from_date, to):
        from_date = datetime.datetime.strptime(self.kwargs.get('from_date'), '%Y-%m-%d')
        to_date = datetime.datetime.strptime(self.kwargs.get('to_date'), '%Y-%m-%d')
        statistics = Statistic.objects.filter(event_date__date__range=[from_date, to_date]).order_by('event_date')
        statistic_serializer = StatisticSerializer(statistics, many=True)
        return Response(statistic_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    @action(detail=False)
    def delete_all(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
