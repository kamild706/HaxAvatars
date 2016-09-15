from django.db import models


class Avatar(models.Model):
    desc = models.CharField(max_length=90)
    team = models.CharField(max_length=4)
    angle = models.PositiveSmallIntegerField()
    text_color = models.CharField(max_length=8)
    color1 = models.CharField(max_length=8)
    color2 = models.CharField(max_length=8, blank=True)
    color3 = models.CharField(max_length=8, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
