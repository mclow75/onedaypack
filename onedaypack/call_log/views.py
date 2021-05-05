from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from call_log.models import Advice
from call_log.serializers import AdviceSerializer


class AdviceViewSet(ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer

