from django.db import models


class Faculty(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Chair(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    chair = models.ForeignKey(Chair, null=True, on_delete=models.SET_NULL)


class Group(models.Model):
    objects = None
    name = models.CharField(max_length=100, null=False, blank=False)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images', null=True)
