from rest_framework.serializers import ModelSerializer
from .models import Websites


class WebsitesSerializer(ModelSerializer):
    class Meta:
        model = Websites
        fields = '__all__'