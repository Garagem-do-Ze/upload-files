from django.db import models

class Document(models.Model):
    first_name = models.CharField(max_length=220)
    second_name = models.CharField(max_length=220)
    email = models.EmailField(max_length = 254, blank=True)
    docname = models.CharField(max_length=220, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    details = models.TextField(default='')

    def __str__(self):
        return self.docname
