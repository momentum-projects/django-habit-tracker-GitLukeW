from django.db import models
from django.contrib.auth.models import AbstractUser
from pickle import TRUE

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Habit(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user_habits', 
        null=TRUE)
    habit = models.CharField(max_length=250)
    target_goal = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.habit}'
