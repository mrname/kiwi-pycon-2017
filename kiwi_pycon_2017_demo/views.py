from math import copysign

from django_q.tasks import async
from rest_framework import viewsets

from .models import Widget
from .serializers import WidgetSerializer


class WidgetViewSet(viewsets.ModelViewSet):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()

    def create(self, *args, **kwargs):
        task_id = async(copysign, 2, -2)
        print('Created super important task with id {0}'.format(task_id))
        return super().create(*args, **kwargs)
