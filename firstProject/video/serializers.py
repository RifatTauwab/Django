from rest_framework.serializers import ModelSerializer
from .models import Video


class VideoSerializers(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'