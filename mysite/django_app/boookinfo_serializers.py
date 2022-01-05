from rest_framework import  serializers

class bookinfoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20)
    bpub_data = serializers.DateField()