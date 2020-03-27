from rest_framework import serializers
import datetime
from .models import Task
from django.core.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):

    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    person_id = serializers.IntegerField()

    class Meta:
        model = Task
        fields = ('date', 'start_time', 'end_time', 'person_id')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.person_id = validated_data.get('person_id', instance.person_id)
        instance.save()
        return instance

    def validate(self, data):
        try:
            if data['date'] < datetime.date.today():
                raise ValidationError("The date cannot be in the past!")
            elif data['end_time'] < data['start_time']:
                raise ValidationError("The end_time cannot be before start_time!")
            elif (data['date'] == datetime.date.today() and data['end_time'] < datetime.datetime.now().time()) or \
                (data['date'] == datetime.date.today() and data['start_time'] < datetime.datetime.now().time()):
                raise ValidationError("The time cannot be in the past!")
        except TypeError:
            raise ValidationError('Incorrect value of date or time')
        return data

