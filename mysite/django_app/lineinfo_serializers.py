from rest_framework import  serializers

class lineinfoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    line = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    value = serializers.IntegerField()
