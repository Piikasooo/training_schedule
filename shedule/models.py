from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Traning {self.person} from {self.start_date}, to {self.end_date} '

