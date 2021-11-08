from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=70, blank=False, default=None)
    surname = models.CharField(max_length=64, blank=False, default=None)
    address = models.CharField(max_length=64, blank=False, default=None)
    phone_number = models.IntegerField(max_length=64, validators=[], blank=True,
                                       null=True)
    url = models.URLField(max_length=64, blank=True, default=None,
                          validators=[])
    image = models.ImageField(upload_to="images/", blank=True)

    class Meta:
        unique_together = ('name', 'surname')



