from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class Task(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} {self.person} traning from {self.start_time}, to {self.end_time} '

    def clean(self):
        try:
            if self.date < datetime.date.today():
                raise ValidationError("The date cannot be in the past!")
            elif self.end_time < self.start_time:
                raise ValidationError("The end_time cannot be before start_time!")
        except TypeError:
            raise ValidationError('Incorrect value of date or time')

