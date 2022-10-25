from rest_framework import serializers
from .models import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cpc'] = format(instance.cost/instance.clicks, '.3f')
        representation['cpm'] = format(instance.cost/instance.views * 1000, '.3f')
        return representation
