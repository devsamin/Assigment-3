from django.db import models
from Category.models import CategoryModel
# Create your models here.

class TaskModel(models.Model):
    Task_title = models.CharField(max_length=50)
    Task_discription = models.CharField(max_length=100)
    Is_completed = models.BooleanField(default=False)
    Task_assign_date = models.DateField()
    categories = models.ManyToManyField(CategoryModel)
    def __str__(self):
        return self.Task_title