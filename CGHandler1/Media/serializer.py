from rest_framework.serializers import ModelSerializer
from .models import Media, Media_Statistics


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'name', 'type', 'status')

class Media_StatisticsSerializers(ModelSerializer):
    class Meta:
        model = Media_Statistics
        fields = '__all__'