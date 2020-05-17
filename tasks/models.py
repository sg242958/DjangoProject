from django.db import models

# it's model field  where our data'll stored
class Detail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    tz = models.CharField(max_length=30, null=True)
    emails = models.EmailField(max_length=20, default=0, null=True)
    text = models.CharField(max_length=300, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.emails




