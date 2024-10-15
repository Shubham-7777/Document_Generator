from django.db import models

class Lender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Borrower(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DocumentTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.FileField(upload_to='templates/')
    
    def __str__(self):
        return self.name

class ExcelUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
