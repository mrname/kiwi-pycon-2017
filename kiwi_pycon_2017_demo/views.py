from rest_framework import viewsets

from .models import Widget
from .serializers import WidgetSerializer


class WidgetViewSet(viewsets.ModelViewSet):
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()
