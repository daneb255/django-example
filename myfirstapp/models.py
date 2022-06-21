from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Webpage(models.Model):
    topic_id = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    webpage_id = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    access_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.webpage_id.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
