from django.db import models

class Property(models.Model):
    loan_number = models.CharField(max_length=30)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    interest_rate = models.FloatField()
    loan_amount = models.FloatField()
    text_representation = models.CharField(max_length=255)
    rehab_withhold = models.FloatField()
    funding_date = models.DateField()
    maturity_date = models.DateField()
    monthly_payment = models.FloatField()
    default_rate = models.FloatField()
    
    def __str__(self):
        return self.loan_number
    
    class Meta:
        verbose_name_plural = "Properties"


class Lender(models.Model):
    name = models.CharField(max_length=30)
    street_address1 = models.CharField(max_length=50)
    street_address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Borrower(models.Model):
    name = models.CharField(max_length=30)
    street_address1 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    signer = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Gurrantor(models.Model):
    name = models.CharField(max_length=30)
    street_address1 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


class CoLender(models.Model):
    name = models.CharField(max_length=30)
    street_address1 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    