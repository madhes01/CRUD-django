from django.db import models
from django.db import connections


class Employee(models.Model):
    eid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = "employee"


