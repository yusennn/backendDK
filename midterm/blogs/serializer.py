from rest_framework import serializers
from blogs.models import Blog


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, allow_null=False)
    description = serializers.CharField(allow_null=True)
    owner = serializers.CharField(max_length=255, allow_null=False)

    def create(self, validated_data):
        blog = Blog(**validated_data)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

