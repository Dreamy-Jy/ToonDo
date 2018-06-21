from django.db import models

class Todo(models.Model):
    complete = models.BooleanField(default=False)
    title = models.CharField(max_length=50, help_text="The Todo's name")

    def __str__(self):
        return  self.title