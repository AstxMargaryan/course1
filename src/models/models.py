from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.FloatField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def update(self, new_rating):
        self.rate = (self.rate * self.count + new_rating) / (self.count + 1)
        self.count += 1
        self.save()

