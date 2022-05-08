from django.db import models

# Create your models here.


class Mark(models.Model):
    enroll = models.CharField(max_length=45, null=False)
    rollno = models.IntegerField()
    name = models.TextField(null=False)
    eti1 = models.IntegerField()
    eti2 = models.IntegerField(default=20)
    mgt1 = models.IntegerField()
    mgt2 = models.IntegerField(default=20)
    wbp1 = models.IntegerField()
    wbp2 = models.IntegerField(default=20)
    pwp1 = models.IntegerField()
    pwp2 = models.IntegerField(default=20)
    mad1 = models.IntegerField()
    mad2 = models.IntegerField(default=20)

    def __str__(self) -> str:
        return self.name

