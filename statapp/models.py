from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name="email")
    message = models.TextField(verbose_name="message")
    status = models.TextField(verbose_name="status")
    date = models.DateTimeField(verbose_name="date")

    class Meta:
        verbose_name = "log"
        verbose_name_plural = "log's"

    def __str__(self):
        return self.email
# Create your models here.
