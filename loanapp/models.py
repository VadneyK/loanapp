
from django.db import models
from django.contrib.postgres.fields import JSONField

class Application(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='applications', on_delete=models.CASCADE) # new

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title