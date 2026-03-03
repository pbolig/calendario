from django.db import models
from django.contrib.auth.models import User

class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendars')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class Category(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ('calendar', 'name')

    def __str__(self):
        return f"{self.name} - {self.calendar.name if self.calendar else 'Global'}"

class Event(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='calendar_events')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.description[:20]}"

class StickyNote(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='stickynotes', null=True, blank=True)
    text = models.TextField()
    color = models.CharField(max_length=20, default="#ffff88")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
