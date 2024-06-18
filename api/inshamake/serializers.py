from rest_framework import serializers

class InkuruZinshaSer(serializers.Serializer):
    inkuru = serializers.CharField()