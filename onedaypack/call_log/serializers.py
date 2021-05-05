from rest_framework.serializers import ModelSerializer

from call_log.models import Advice


class AdviceSerializer(ModelSerializer):
     class Meta:
         model = Advice
         fields = ['id', 'topic', 'duration', 'department']

