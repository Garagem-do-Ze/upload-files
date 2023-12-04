from django.db import models

class Document(models.Model):
    docname = models.CharField(max_length=220, default='DOC')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.docname
