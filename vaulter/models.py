from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Safe(models.Model):
    service = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False)
    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    pwned = models.BooleanField(default=False)
    date_modified_last = models.DateTimeField(default=timezone.now)
    vaulter = models.ForeignKey(User, on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse("safe-detail", kwargs={'pk': self.pk})

