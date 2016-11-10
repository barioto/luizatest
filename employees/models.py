from django.db import models


class Departament(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    departament = models.ForeignKey(Departament)

    def __str__(self):
        return self.name
