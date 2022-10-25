from django.contrib import admin
from .models import Statistic


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    pass
# Register your models here.
