from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    deadline = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item, self.deadline
