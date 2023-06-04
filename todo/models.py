from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=250)
    create_date = models.DateTimeField("Date made")
    due_date = models.DateTimeField("Task due date and time")
    done = models.BooleanField("Task id done")
    

    def __str__(self):
        return self.task_name
    

