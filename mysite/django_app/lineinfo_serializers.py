from rest_framework import  serializers

class lineinfoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    line = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    value = serializers.IntegerField()
