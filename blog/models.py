from django.db import models
from users.models import CustomUser


class Task(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
