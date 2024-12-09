from django.db import models


class DocumentTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.name
