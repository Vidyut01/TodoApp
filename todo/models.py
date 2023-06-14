from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=250)
    create_date = models.DateTimeField("Date made")
    due_date = models.DateTimeField("Task due date and time")
    done = models.BooleanField("Task id done")
    user = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return str(self.task_name)
    

    

