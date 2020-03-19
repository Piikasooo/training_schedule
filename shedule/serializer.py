from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('date', 'start_time', 'end_time', 'person_id')

        date = serializers.DateField()
        start_time = serializers.TimeField()
        end_time = serializers.TimeField()
        person_id = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.person_id = validated_data.get('person_id', instance.person_id)
        instance.save()
        return instance
