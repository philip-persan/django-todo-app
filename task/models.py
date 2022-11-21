from django.db import models

from users.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User',
        blank=True,
        null=True
    )
    description = models.CharField(
        verbose_name='Descriptions',
        max_length=255,
        blank=False,
        null=True,
    )
    date_created = models.DateTimeField(
        verbose_name='Added on Date',
        auto_now_add=True,
        blank=False
    )
    completed = models.BooleanField(
        verbose_name='Completed',
        blank=True,
        null=False,
        default=False
    )
    date_completed = models.DateTimeField(
        verbose_name='Completed at',
        auto_now=False,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        task = self.description
        return task

    @property
    def completion_time(self):
        date_created = self.date_created
        date_completed = self.date_completed
        time = date_completed - date_created
        return time

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Task's"
        ordering = ["-date_created", "completed"]
