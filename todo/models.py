from django.db import models


# Create your models here.

class Note(models.Model):
    text = models.TextField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField()

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

    def  __str__(self):
        return f"{self.text}"
