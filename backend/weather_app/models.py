from django.db import models
from user_app.models import UserAccount

class FrequencyChoices(models.TextChoices):
    DAY = 'day', 'Day'
    MONTH = 'month', 'Month'
    YEAR = 'year', 'Year'


class UserCriteria(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    comparison_operator = models.CharField(max_length=2, choices=[(
        '<', '<'), ('>', '>'), ('<=', '<='), ('>=', '>='), ('==', '==')])
    value = models.FloatField()
    frequency = models.CharField(
        max_length=10, choices=FrequencyChoices.choices)
    is_statisfied = models.BooleanField(default=False)
