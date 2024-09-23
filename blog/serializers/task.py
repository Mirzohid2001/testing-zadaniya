from rest_framework import serializers
from blog.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'created_at', 'owner')
        read_only_fields = ('id', 'created_at', 'owner')

        def validate_title(self, value):
            if not value:
                raise serializers.ValidationError('Title is required')
            return value

        def create(self, validated_data):
            request = self.context.get('request')
            task = Task.objects.create(
                owner=request.user,
                **validated_data
            )

            return task

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.status = validated_data.get('status', instance.status)
            instance.save()
            return instance
